import os

from django.contrib.auth.models import Group
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from api.models import User
import requests
import json


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "geolocation")


class CustomUserSerializer(UserDetailsSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'geolocation')
        model = User


class CustomRegisterSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request, *args, **kwargs):
        response = requests.get(
            f"https://ipgeolocation.abstractapi.com/v1/?api_key={os.getenv('IP_GEO_LOCATION_API_KEY', '')}")
        location = json.loads(response.content)
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('email', '')
        user.set_password(self.cleaned_data.get('password1', ''))
        user.email = self.cleaned_data.get('email', '')
        user.role = self.cleaned_data.get('role', '')
        user.geolocation = location
        group = Group.objects.filter(name='user').first()
        user.save()
        if group:
            user.groups.set([group])
            user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            return data
        else:
            raise serializers.ValidationError('Email and password are required.')
