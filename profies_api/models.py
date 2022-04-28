import email
import imp
from re import U
from struct import pack
from tkinter import N
from unicodedata import name
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager 

class UserProfileManager(BaseUserManager):
    """ manage user profiles"""
    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """create n save new supusr"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff =  True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ db model for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['name']

    def get_full_name(self):
        """ retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """ return string represntation of user"""
        return self.email