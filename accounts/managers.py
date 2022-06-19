from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager as BaseManager
from django.utils.translation import gettext_lazy as _


class BaseUserManager(BaseManager):

    def _create_user(self, email, password, is_staff, is_superuser, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError(_('وارد کردن شماره تلفن اجباری است'))

        if email:
            email = self.normalize_email(email)

        now = timezone.now()

        user = self.model(
            email=email,
            phone_number=phone_number,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, phone_number=None, **extra_fields):
        return self._create_user(email, password, False, False, phone_number, **extra_fields)

    def create_superuser(self, password, phone_number, email=None, **extra_fields):
        user = self._create_user(email, password, True, True, phone_number, **extra_fields)
        user.save(using=self._db)
        return user

