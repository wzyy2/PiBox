from django.db import models
from django.contrib.auth.models import AbstractUser

UPLOAD_ROOT='pibox_upload/house_plan'

class PiUser(AbstractUser):
    new_field = models.CharField(max_length=100)


class PiSettings(models.Model):
    ip          = models.IPAddressField(default="127.0.0.1")
    port     = models.IntegerField(default=3333)


class Device(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField(default='')
    location = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()            


class Home(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = UPLOAD_ROOT)         

