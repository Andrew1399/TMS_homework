from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from users import services
from users.api.v1.serializers import UserSignUpSerializer


class SignUpView(APIView):

    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = services.auth_service.signup_user(serializer.data)

        return Response({
            'token': user.token.key,
            'user_id': user.pk
        })


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        request.user.token.delete()
        return Response(status=status.HTTP_200_OK)