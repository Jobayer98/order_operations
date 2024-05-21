from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from .models import Order, OrderStatus, Payment, Product
from .serializers import (OrderSerializer,OrderStatusSerializer,
                          ProductSerializer, PaymentSerializer)
