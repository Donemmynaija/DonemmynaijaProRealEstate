from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROLE = (
    ('agent', 'Agent'),
    ('landlord', 'Landlord'),
    ('developer', 'Developer'),
    ('user', 'User'),
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    

    def __str__(self):
        return self.fullname