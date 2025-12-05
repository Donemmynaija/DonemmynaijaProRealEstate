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
        fields = ['fullname', 'email', 'phone_number', 'role', 'profile_picture']

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile
        fields = ['fullname', 'email', 'phone_number', 'role', 'profile_picture', 'password', 'confirm_password']

def validate(self, data):
    if data['password'] != data['confirm_password']:
        raise serializers.ValidationError("Passwords do not match.")
    if User.objects.filter(email=data['email']).exists():
        raise serializers.ValidationError("Email is already in use.")
    return data

def create(self, validated_data):
        email=validated_data.pop('email'),
        password=validated_data.pop('password')
        confirm_password=validated_data.pop('confirm_password')
        user = User.objects.create_user(email=email, password=password)
        profile= Profile.objects.create(
                               user=user,
                               full_name= validated_data('fullname'),
                               phone_number= validated_data('phone_number'),
                               role= validated_data('role'),
                               profile_picture= validated_data('profile_picture')
                    
                               
                               )
        send_welcome_email(email, profile.fullname)
        return profile