from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_confirmed_email = models.BooleanField(
        default=False,
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
    )
    birthday_date = models.DateField(
        null=True,
        blank=True,
        default=None,
    )
    is_active = models.BooleanField(
        default=False,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email, ], **kwargs)
