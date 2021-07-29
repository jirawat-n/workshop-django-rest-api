from django.contrib import admin
from .models import category,Product,product_image,cart,invoice,invoice_item
# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
admin.site.register(category)
admin.site.register(Product)
admin.site.register(product_image)
admin.site.register(cart)
admin.site.register(invoice)
admin.site.register(invoice_item)
