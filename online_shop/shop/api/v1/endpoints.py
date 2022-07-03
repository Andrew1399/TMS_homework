from shop.models import Product, Cart, CartItem, Category, Order, OrderItem, Brand
from shop.api.v1 import serializers
from django.http import Http404
from django.db.models import F, FloatField, Sum
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from shop.api.v1.services import CartService


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductBaseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'price']

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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = serializers.CartAddProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = request.user

        cart_serivce = CartService(user)
        cart_serivce.add_product(serializer.data)

        return Response(data=cart_serivce.get_user_cart(), status=status.HTTP_200_OK)


class OrderCreateView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def perform_create(self, serializer):
        try:
            purchaser_id = self.request.data['user']
            user = User.objects.get(pk=purchaser_id)
        except:
            raise ValidationError("User wasn't found")
        cart = user.cart
        for cart_item in cart.items.all():
            if cart_item.product.available_inventory - cart_item.quantity < 0:
                raise ValidationError(
                    'We do not have enough inventory of ' + str(cart_item.product.title) +
                    'to complete your purchase. Sorry, we will restock soon'
                )
        total_aggregated_dict = cart.items.aggregate(total_price=Sum(F('quantity') * F('product__price'), output_field=FloatField()))

        order_total = round(total_aggregated_dict['total'], 2)
        order = serializer.save(user=user, total_price=order_total)

        order_items = []
        for cart_item in cart.items.all():
            order.items.append(OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity))
            cart_item.product.available_inventory -= cart_item.quantity
            cart_item.product.save()

        OrderItem.objects.bulk_create(order_items)
        cart.items.clear()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer