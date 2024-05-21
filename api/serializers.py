from rest_framework import serializers
from .models import Product, Order
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
                
class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(write_only=True)
    product_id = serializers.IntegerField(write_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    payment_amount = serializers.DecimalField(max_digits=9, decimal_places=2, write_only=True, source="amount")
    payment_method = serializers.CharField(write_only=True)
    class Meta:
        model = Order
        fields = ['id','order_date', 'order_status', 'quantity', 'product_id', 'customer_id', 'payment_amount', 'payment_method']
        read_only_fields = ['order_status', 'order_date']
        
class OrderDetailSerializer(serializers.ModelSerializer):
    payment_amount = serializers.DecimalField(max_digits=9, decimal_places=2, source="amount")
    order_status_id = serializers.IntegerField(write_only=True)
    order_status = serializers.StringRelatedField()
    unit_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'unit_price', 'quantity', 'total_price', 'order_status', 'order_date', 'payment_method', 'payment_amount', 'order_status_id']
        read_only_fields = ['customer', 'product', 'order_status', 'order_date', 'unit_price', 'total_price']
    
    def get_unit_price(self, obj):
        return obj.product.unit_price
    
    def get_total_price(self, obj):
        return obj.quantity * obj.product.unit_price
    