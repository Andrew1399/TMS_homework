from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import Product, Cart, CartItem, Category, Order, OrderItem, Brand


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class ProductBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=50)
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    available_inventory = serializers.IntegerField()


class ProductCreateSerializer(ProductBaseSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductUpdateSerializer(ProductBaseSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductReadSerializer(ProductBaseSerializer):
    pass


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'updated_at', 'items', )


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductBaseSerializer(required=False)

    class Meta:
        model = CartItem
        fields = (
            'id', 'cart', 'product', 'price', 'quantity')


class CartAddProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Order
        fields = ('user', 'total_price', 'created_at', 'updated_at', 'products')


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    # product = ProductReadSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'price', 'quantity')

