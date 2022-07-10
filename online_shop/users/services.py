from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


class AuthService:

    def signup_user(self, user_sign_up_data: dict) -> User:
        username = user_sign_up_data['username']
        password = user_sign_up_data['password_1']

        user: User = User.objects.create_user(username=username, password=password)

        Token.objects.create(user=user)
        print(Token.objects.all)

        return user

auth_service = AuthService()