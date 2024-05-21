from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer


class IndexView(APIView):
    def get(self, request):
        return Response({"url": "http://localhost:8000/api/orders"})
    
    
class OrdersView(APIView):
    
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderDetailView(APIView):
    
    def get(self, request, pk):
        orders = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data, status=status.HTTP_200_OK)