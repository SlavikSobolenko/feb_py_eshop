from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return user.order.all()

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return obj

class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        order = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return order.orderitem.all()

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_object(self):
        obj = get_object_or_404(OrderItem, pk=self.kwargs.get('orderitem_id'))
        return obj



