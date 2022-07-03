from django.urls import include, path

from users.api.v1.endpoints import SignUpView, LoginView, LogoutView


auth_urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())

]

urlpatterns = [
    path('users/auth/', include(auth_urlpatterns)),
]