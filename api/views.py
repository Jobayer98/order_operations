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
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
class OrderDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Order, pk=pk)
    
    def get(self, request, pk):
        orders = self.get_object(pk)
        serializer = OrderDetailSerializer(orders)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderDetailSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderDetailSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)