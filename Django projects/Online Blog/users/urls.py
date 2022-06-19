from django.urls import path, include
from users import views
from django.contrib.auth.views import \
    (PasswordChangeView, PasswordChangeDoneView)
from django.urls import reverse_lazy


app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register_writer/', views.register_writer, name='register_writer'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('users:password_change_done')),
        name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),
    path('<str:username>/follow/', views.profile_follow, name='profile_follow'),
    path('<str:username>/unfollow/', views.profile_unfollow, name='profile_unfollow'),
]