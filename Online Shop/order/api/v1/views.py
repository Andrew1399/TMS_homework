from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from order.models import Cart, Order, OrderItem
from order.serializers import (
    CartSerializer, UserSerializer,
    CartItemAddSerializer, OrderSerializer, OrderItemSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        carts = Cart.objects.all()
        return carts


class CartItemAddView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemAddSerializer


class CartItemDeleteView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Cart.objects.all()
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Order.objects.all()
        return queryset


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = OrderItem.objects.all()
        return queryset