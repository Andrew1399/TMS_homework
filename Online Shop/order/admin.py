from django.contrib import admin
from order.models import Order, Cart, OrderItem

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
