from django.urls import path, include
from shop.api.v1 import endpoints
from rest_framework import routers

router = routers.DefaultRouter()
router.register('brands', endpoints.BrandViewSet, basename='brands')
router.register('carts', endpoints.CartViewSet, basename='carts')
router.register('cart_items', endpoints.CartItemViewSet, basename='cart_items')
router.register('order_items', endpoints.OrderItemViewSet)

urlpatterns = [
    path('product_list/', endpoints.ProductList.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', endpoints.ProductDetail.as_view(), name='product_detail'),
    path('cart_item/delete/<int:pk>/', endpoints.CartItemDelView.as_view()),
    path('carts/delete/<int:pk>/', endpoints.CleanCartView.as_view()),
    path('carts_cache/', endpoints.CartAddItemApiView.as_view(), name='cart_cache'),
    path('create_order/', endpoints.OrderCreateView.as_view(), 'create_order'),
    path('order_list/', endpoints.OrderListView.as_view(), name='order_list'),
    path('order_detail/<int:pk>/', endpoints.OrderDetailView.as_view(), name='order_detail'),
    path('', include(router.urls))
]