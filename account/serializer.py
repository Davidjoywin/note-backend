from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if self.context['request'].user.is_authenticated:
            raise ValidationError({"auth": "A user is already logged in."})
        user = authenticate(username=data['username'], password=data['password'])
        # user = authenticate(**data)
        if not user:
            raise ValidationError({"auth": "Incorrect username or password"})
        return user

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def validate(self, data):
        if self.context['request'].user.is_authenticated:
            raise ValidationError({"auth": "A user is already logged in"})
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

    