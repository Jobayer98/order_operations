from django.contrib import admin
from .models import Order, OrderStatus, Product

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Product)