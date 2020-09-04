from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user"""
    
    def create_user(self, name, email, password=None):
        """create new user"""
        if not email:
            raise ValueError("user must have email")

        email = self.normalize_email(email) #to normalise email
        user = self.model(email=email, name=name) #create the user

        user.set_password(password)
        user.save(using=_db)

        return user

    def create_superuser(self, email, name, password):
        """create and save superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of the user"""
        return self.name

    def __str__(self):
        """string representationof our user!"""
        return self.email