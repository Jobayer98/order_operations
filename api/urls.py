from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.OrdersView.as_view(), name="order-list"),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name="order-detail")
]