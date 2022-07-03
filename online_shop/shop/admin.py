from django.contrib import admin
from shop.models import Product, Cart, CartItem, Category, Order, OrderItem, Brand

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Brand)
