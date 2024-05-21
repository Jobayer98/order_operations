from django.contrib import admin
from .models import Order, OrderItem, OrderStatus, Payment, Product

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)
admin.site.register(Payment)
admin.site.register(Product)