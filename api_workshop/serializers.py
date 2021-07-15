from rest_framework import serializers
from django.contrib.auth.models import User
from .models import category, Product, product_image, cart, invoice, invoice_item
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.exceptions import NotFound, NotAuthenticated, AuthenticationFailed, ParseError
from versatileimagefield.serializers import VersatileImageFieldSerializer


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            data['expire_id'] = int(refresh.access_token.lifetime.total_seconds())
            data['token_type'] = str(refresh.token_type)
            return data
        except:
            raise ParseError({'msg': 'Login Fail'})
        return super().validate(attrs)


class TokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            refresh = RefreshToken(attrs['refresh'])
            data['token_type'] = str(refresh.token_type)
            data['expire_id'] = int(
                refresh.access_token.lifetime.total_seconds())
            data['refresh_token'] = str(refresh)
            return data
        except:
            raise ParseError({'msg': 'Login Fail'})


class RegisterSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=10, error_messages={"blank": "ชื่อผู้ใช้เป็นค่าว่าง กรุณากรอกชื่อผู้ใช้งาน"})
    password = serializers.CharField(max_length=10, error_messages={
                                     "blank": "รหัสผ่านเป็นค่าว่าง กรุณากรอกรหัสผ่าน"})

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def validate_password(self, password):
        if password is None:
            raise ValidationError('กรุณาใส่รหัสผ่าน')
        if len(password) < 8:
            raise ValidationError('รหัสผ่านน้อยกว่า 8 ตัว')
        return password

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        user.save()
        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'image', 'name', 'is_enabled', 'detail']


class Product_Image_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product_image
        fields = ['id', 'image']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image_product = Product_Image_Serializer(many=True, read_only=True)
    image = VersatileImageFieldSerializer(sizes='person_headshot')

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price',
                  'image', 'is_enabled', 'image_product']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.CharField(max_length=10,
                                    error_messages={
                                        "blank": "กรุณากรอกรหัสสินค้า",
                                        'write_only': True
                                    })
    quantity = serializers.IntegerField(error_messages={
        "blank": "จำนวนสินค้านี้ต้องมากกว่า 0",
        'write_only': True
    })

    class Meta:
        model = cart
        fields = ['id', 'quantity', 'total', 'product']

    def validate_product(self, product):
        try:
            is_enableds = Product.objects.get(pk=int(product))
        except:
            raise ValidationError('ไม่พบสินค้า')

        if not is_enableds.is_enabled:
            raise ValidationError('สินค้านี้ถูกปิดการใช้งาน')
        return product

    def validate_quantity(self, quantity):
        if quantity < 1:
            raise ValidationError('จำนวนสินค้านี้ต้องมากกว่า 0')
        return quantity


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoice
        fields = ['url', 'id', 'created_datetime',
                  'updated_datetime', 'status', 'total']


class Invoice_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = invoice_item
        fields = ['id', 'product', 'invoice',
                  'created_datetime', 'quantity', 'total']


class Invoice_Detail_Serializer(serializers.ModelSerializer):
    invoice_item = Invoice_Item_Serializer(many=True, read_only=True)

    class Meta:
        model = invoice
        fields = ['id', 'created_datetime', 'updated_datetime',
                  'status', 'total', 'invoice_item']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoice
        fields = ['id']
