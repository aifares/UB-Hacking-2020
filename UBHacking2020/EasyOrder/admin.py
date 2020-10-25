from django.contrib import admin
from .models import Restaurant, Product, CartItem,Cart

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
