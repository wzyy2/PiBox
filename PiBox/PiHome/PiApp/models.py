from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class PiUser(AbstractUser):
    new_field = models.CharField(max_length=100)


class PiSettings(models.Model):
     ip          = models.IPAddressField(default="127.0.0.1")
     port     = models.IntegerField(default=3333)