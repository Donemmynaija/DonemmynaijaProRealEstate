from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.Serializer):
    class Meta: 
        model = User
        fields = ['username', 'email']

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserSerializer
        fields = ['fullname', 'email', 'phone_number', 'role', 'profile_picture']

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile
        fields = ['fullname', 'email', 'phone_number', 'role', 'profile_picture', 'password', 'confirm_password']