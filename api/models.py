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
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    order_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.pk
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f"{self.product.name} | {self.quantity}"
    
class Payment(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self) -> str:
        return self.pk