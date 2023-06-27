from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    geolocation = models.JSONField(null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
