from django.db import models
from django.contrib.auth.models import User

"""
Create user
Create superuser
set password
change password
how to authenticate user
how to login user
how to logout user
login_required_decorator

access user in view
access user in templates

default auth views
default auth form
    - subclassing auth forms
attaching default auth urls 

Groups
Permissions

Customization 
    - writing custom auth backends
    - extending user model
        - 3 ways to extend user model
            - Create user profile model
            - Extend User model with AbstractUser
            - Extend User model with AbstractBaseUser
"""

# 1st way, create profile model with user relation


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=10, blank=True)
    # role = models.CharField(max_length=10, blank=True)
    # dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.type
