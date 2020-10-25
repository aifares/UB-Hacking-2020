from django.contrib import admin
from .models import Restaurant, Product, CartItem,Cart,Category

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)