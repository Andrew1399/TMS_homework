from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from order.models import Cart, Order, OrderItem
from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'is_superuser')


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'quantity', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        rep = super(CartSerializer, self).to_representation(instance)
        rep['product'] = instance.product.title
        rep['user'] = instance.user.username
        return rep


class CartItemAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ('quantity', 'product_id', 'user_id')
        extra_qwargs = {'quantity': {'required': True}, 'product_id': {'required': True}, 'user_id': {'required': True}}

    def create(self, validated_data):
        product = get_object_or_404(Product, id=validated_data['product_id'])
        user = get_object_or_404(User, id=validated_data['user_id'])

        cart_item = Cart.objects.create(
            product=product,
            user=user,
            quantity=validated_data['quantity']
        )
        cart_item.save()
        return cart_item


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'user', 'cart', 'order_total', 'created_at', 'updated_at',)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'price', 'quantity',)

    def to_representation(self, instance):
        rep = super(OrderItemSerializer, self).to_representation(instance)
        rep['product'] = instance.product.title
        return rep
