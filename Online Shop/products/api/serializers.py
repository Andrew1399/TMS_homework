from rest_framework import serializers
from products.models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'slug',)


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'slug', 'created_at', 'updated_at',)


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('title', 'country',)
