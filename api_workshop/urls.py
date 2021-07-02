from api_workshop import views
from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api_workshop.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# product_detail = ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

category_list = CategotyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategotyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

product_image_list = Product_Image_ViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_image_detail = Product_Image_ViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
# cart_list = CartViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# cart_detail = CartViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# invoice_list = InvoiceViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# invoice_detail = InvoiceViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product_image', views.Product_Image_ViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'invoice', views.InvoiceViewSet)
router.register(r'invoice_item', views.Invoice_Item_ViewSet)

urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    path('api/token/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', RefrestView.as_view(), name='token_refresh'),

    path('api/register/', RegisterApi.as_view()),

    path('', api_root),

    path('product/', ProductViewSet.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductViewSetDetail.as_view(), name='product-detail'),

    path('categoty/', category_list, name='category-list'),
    path('categoty/<int:pk>/', category_detail, name='category-detail'),

    path('product_image/', product_image_list, name='product_image-list'),
    path('product_image/<int:pk>/', product_image_detail,name='product_image-detail'),

    path('product_image/', product_image_list, name='product_image-list'),
    path('product_image/<int:pk>/', product_image_detail,name='product_image-detail'),

    path('cart/', CartViewSet.as_view(), name='cart-list'),
    path('cart/<int:pk>/', EditCartQuanlity.as_view(), name='cart-edit'),
    
    path('invoice_item/', InvoiceViewSet.as_view(), name='invoice_item-list'),
    path('invoice_item/<int:pk>/', InvoiceViewSet.as_view(),name='invoice_item-detail'),

    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


