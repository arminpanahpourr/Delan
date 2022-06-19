from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class User(AbstractBaseUser, BaseModel):
    phone_number = models.CharField(max_length=12)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email
