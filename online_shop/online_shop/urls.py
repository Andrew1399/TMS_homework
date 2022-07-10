from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('shop.urls')),
    path('api/v1/', include('users.urls'))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]