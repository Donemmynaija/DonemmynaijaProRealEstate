from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .utils import send_welcome_email

class UserSerializer(serializers.Serializer):
    class Meta: 
        model = User
        fields = ['username', 'email']

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserSerializer
        fields = ['fullname', 'email', 'phone_number', 'role', 'profile_picture', 'password', 'confirm_password' ]

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullname', 'email', 'phone_number', 'role', 'password', 'confirm_password']

    def create(self, validated_data):
        profile = Profile.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            password1=validated_data['password'],
            password2=validated_data['confirm_password'],
            role=validated_data['role'],
            password=validated_data('password'),
            confirm_password=validated_data('confirm_password')
        )
        send_welcome_email(profile.email, profile.fullname)
        return profile
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data