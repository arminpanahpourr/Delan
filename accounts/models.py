from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from accounts.managers import BaseUserManager


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    phone_number = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = BaseUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('first_name', 'email')

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email
