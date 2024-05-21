from rest_framework import serializers
from .models import Payment, Product, Order, User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
                
class OrderSerializer(serializers.ModelSerializer):
    order_status = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Order
        fields = ['id','order_date', 'order_status', 'product_id', 'customer_id']
        
class OrderDetailSerializer(serializers.ModelSerializer):
    order_status = serializers.StringRelatedField(read_only=True)
    total_price = serializers.SerializerMethodField()
    unit_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id','product', 'customer', 'order_date', 'order_status', 'unit_price', 'quantity', 'total_price']
        
    def get_total_price(self, obj):
        return obj.quantity * obj.product.unit_price
    
    def get_unit_price(self, obj):
        return obj.product.unit_price
    