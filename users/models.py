from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models

from HW19_2.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=150, verbose_name='First name', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Last name', **NULLABLE)
    phone = PhoneNumberField(unique=True, verbose_name='Phone', **NULLABLE)
    avatar = models.ImageField(verbose_name='avatar', upload_to='users/avatars/', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name = 'country', **NULLABLE)
    token = models.CharField(max_length=150, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


