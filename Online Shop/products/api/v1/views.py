from rest_framework import viewsets
from products.api.serializers import\
    (ProductSerializer, BrandSerializer)
from products.models import Product, Brand


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Brand.objects.all()
        return queryset
