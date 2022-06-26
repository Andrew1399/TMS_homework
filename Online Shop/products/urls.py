from django.urls import path
from products.api.v1 import views
from rest_framework import routers

product_list = views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail = views.ProductViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update',
                                         'delete': 'destroy'})

brand_list = views.BrandViewSet.as_view({'get': 'list', 'post': 'create'})
brand_detail = views.BrandViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update',
                                     'delete': 'destroy'})


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products_v1')
router.register('brands', views.BrandViewSet, basename='brands_v1')


urlpatterns = [
    path('v1/product_list/', product_list, name='product_list'),
    path('v1/product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('v1/brand_list/', brand_list, name='brand_list'),
    path('v1/brand_detail/<int:pk>/', brand_detail, name='brand_detail'),
]