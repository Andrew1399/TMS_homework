from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.v1.endpoints import UserSignUpView, LogoutView


auth_urlpatterns = [
    path('signup/', UserSignUpView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns = [
    path('users/auth/', include(auth_urlpatterns)),
]