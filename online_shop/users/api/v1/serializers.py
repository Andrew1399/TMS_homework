from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings
from rest_framework import serializers


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found! Try again!'
            )
        try:
            payload = api_settings.SIMPLEJWT_PAYLOAD_HANDLER(user)
            jwt_token = api_settings.SIMPLEJWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        finally:
            pass
        return {
            'username': user.username,
            'token': jwt_token
        }
