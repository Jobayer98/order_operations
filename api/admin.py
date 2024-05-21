from django.contrib import admin
from .models import Order, OrderStatus, Payment, Product

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Payment)
admin.site.register(Product)