from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=150)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name

class OrderStatus(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default=1)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, default=1)
    order_date = models.DateTimeField()
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return str(self.pk)
class Payment(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self) -> str:
        return str(self.pk)