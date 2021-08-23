from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Invalid Email')
        ## normalize email, convert second half to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, name, password):
        """Create and save a new super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.__db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self) -> models.CharField:
        """
        Retrieve full name of user
        :return: str
        """
        return self.name

    def get_short_name(self) -> models.CharField:
        """
        Retrieve full name of user
        :return: str
        """
        return self.name

    def __str__(self) -> str:
        """
        Return String representation of User
        :return: str
        """
        return f"Email: {self.email}, Name:{self.name}"
