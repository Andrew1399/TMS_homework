from shop.models import Product, Cart, CartItem, Category, Order, OrderItem, Brand
from shop.api.v1 import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from shop.api.v1.services import CartService, OrderService


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductBaseSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['title', 'category']
    search_fields = ['title']

    def post(self, request, format=None):
        serializer = serializers.ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductReadSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BrandSerializer
    queryset = Brand.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

    @action(detail=True, methods=['get'])
    def add_to_cart(self, request, pk):
        cart_item = CartItem.objects.filter(pk=pk)
        target_item = cart_item.get(pk=pk)
        if target_item.quantity <= 0:
            return Response(
                data={
                    "detail": "this item was sold out, try another one!",
                    "code": "sold_out"})
        target_item.quantity = target_item.quantity + 1
        target_item.save()
        return Response(
            status=status.HTTP_226_IM_USED,
            data={"detail": 'one object added successfully', "code": "done"})

    @action(detail=True, methods=['get'])
    def remove_to_cart(self, request, pk):
        cart_item = CartItem.objects.filter(pk=pk)
        target_item = cart_item.get(pk=pk)
        if target_item.quantity == 0:
            return Response(
                data={
                    "detail": "there is no more items like this in your cart"})
        target_item.quantity = target_item.quantity - 1
        target_item.save()
        return Response(
            status=status.HTTP_226_IM_USED,
            data={'detail': 'one object was deleted'})


class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer


class CartItemDelView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def delete(self, request, pk, format=None):
        cart_item = CartItem.objects.filter(pk=pk)
        target_item = get_object_or_404(cart_item, pk=pk)
        target_item.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})


class CleanCartView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    # This function isn't actual because I used the cache, so I have no need to use it, but it can come in handy

    def delete(self, request, pk, format=None):
        cart = Cart.objects.filter(pk=pk)
        single_cart = get_object_or_404(cart, pk=pk)
        single_cart.delete()
        single_cart.save()
        return Response(status=status.HTTP_226_IM_USED, data={"detail": 'the cart was cleaned successfully'})


class CartAddItemApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = serializers.CartAddProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = request.user

        cart_serivce = CartService(user)
        cart_serivce.add_product(serializer.data)

        return Response(data=cart_serivce.get_user_cart(), status=status.HTTP_200_OK)


class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderCreateView(APIView):

    # This function isn't finished
    def post(self, request):
        user = request.user
        order = request.order

        cart_service = CartService(user)
        cart = cart_service.get_user_cart()

        order_service = OrderService(user)
        order_service.create_order_products(order)

        return Response(data=order_service.create_order(cart), status=200)

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer