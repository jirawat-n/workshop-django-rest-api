from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='images/category', default=None)
    is_enabled = models.BooleanField(default=True)
    detail = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        category, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    image = VersatileImageField(
        'image', upload_to='images/product', ppoi_field='image_ppoi')
    is_enabled = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


class product_image(models.Model):
    product = models.ForeignKey(
        Product, null=True, related_name='image_product', blank=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/category', default=None)

    def __str__(self):
        return self.product.name


class cart(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.product.name

    class Meta:
        unique_together = ['user', 'product']


class invoice(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    total = models.IntegerField(default=0)
    status_choice = (
        ('wait', 'wait'),
        ('sended', 'sended'),
        ('cancle', 'cancle'),
    )
    status = models.CharField(max_length=40, null=True,
                              blank=False, default='wait', choices=status_choice)


class invoice_item(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    invoice = models.ForeignKey(invoice, related_name='invoice_item', null=True, blank=True, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
