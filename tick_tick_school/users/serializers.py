# Django imports
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

# DRF imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Project imports
from .models import User


# Views
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]


class UserCreationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirmation'
        ]

        extra_kwargs = {
            'email': {'validators': [
                UniqueValidator(
                    queryset=User.objects.all(),
                )
            ]}
        }

    def validate(self, data):
        if not data['password_confirmation'] == data['password']:
            return serializers.ValidationError('Las contraseñas no son iguales')
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data)
        token = Token.objects.get_or_create(user=user)
        return user, token.key


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]

