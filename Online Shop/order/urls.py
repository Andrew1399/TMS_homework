from django.urls import path
from rest_framework import routers
from order.api.v1 import views

router = routers.DefaultRouter()
router.register('carts', views.CartViewSet, basename='carts')

order_list = views.OrderViewSet.as_view({'get': 'list', 'post': 'create'})
order_detail = views.OrderViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                           'patch': 'partial_update', 'delete': 'destroy'})

order_item_list = views.OrderItemViewSet.as_view({'get': 'list', 'post': 'create'})
order_item_detail = views.OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'patch': 'partial_update', 'delete': 'destroy'})


urlpatterns = [
    path('v1/cart/', views.CartViewSet.as_view({'get': 'list'}), name='cart'),
    path('v1/cart/add/', views.CartItemAddView.as_view()),
    path('v1/cart/delete/<int:pk>/', views.CartItemDeleteView.as_view({'delete': 'destroy'})),
    path('v1/order_list/', order_list, name='order_list'),
    path('v1/order_detail/<int:pk>/', order_detail, name='order_detail'),
    path('v1/order/item/', order_item_list, name='order_item_list'),
    path('v1/order/item_detail/<int:pk>/', order_item_detail, name='order_item_detail')
]