from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .utils import send_welcome_email

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'email']
 
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer()
        fields = ['fullname', 'username', 'email', 'phone_number', 'role', 'gender', 'profile_picture']

class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile
        fields = ['fullname', 'username', 'email', 'phone_number', 'role', 'gender', 'profile_picture', 'password1', 'password2']

        def validate(self, data):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError("Passwords do not match.")
            
        def create(self, validated_data):
            username = validated_data.pop('username')
            email = validated_data.pop('email')
            password = validated_data.pop('password1')

            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(user = user,
                                             fullname = validated_data['fullname'],
                                             phone_number = validated_data['phone_number'],
                                             role = validated_data['role'],
                                             gender = validated_data['gender'],
                                             profile_picture = validated_data['profile_picture'],
                                             )
            send_welcome_email(email, username)
            return profile