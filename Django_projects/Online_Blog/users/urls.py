from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
]