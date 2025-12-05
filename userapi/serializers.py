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
        
        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError("Passwords do not match.")
            return data
        
        def create(self, validate_data):
            username = validate_data.pop('username')
            email = validate_data.pop('email')
            password = validate_data.pop('password1')

            user = User.objects.create_user(username=username,password=password,email=email)
            profile = Profile.objects.create(
                user = user,
                fullname = validate_data['fullname'],
                email = validate_data['email'],
                phone_number = validate_data['phone_number'],
                role = validate_data['role'],
                password = validate_data['password'],
            )
            #send email
            send_welcome_email(email, validate_data['fullname'])
            return profile