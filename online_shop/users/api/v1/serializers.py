from rest_framework import serializers
from django.contrib.auth.models import User


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password_1 = serializers.CharField()
    password_2 = serializers.CharField()

    def validate_username(self, value):

        lower_username = value.lower()

        if User.objects.filter(email__iexact=lower_username).exists():
            raise serializers.ValidationError('Such username already exist')

        return value

    def validate(self, data):
        if data['password_1'] != data['password_2']:
            raise serializers.ValidationError('Password does not match!')

        return data
