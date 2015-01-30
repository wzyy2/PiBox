#coding=utf-8
'''
# The modules contains PiApp's models 

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.db import models
from django.contrib.auth.models import AbstractUser
from PiHome import settings

import os

UPLOAD_ROOT = 'pibox_upload'
UPLOAD_ROOT_HOUSR_PLAN='pibox_upload/house_plan/'
UPLOAD_ROOT_PIC='pibox_upload/pic_datapoint/'


class PiUser(AbstractUser):
    new_field = models.CharField(max_length=100)


class PiSettings(models.Model):
    ip       = models.GenericIPAddressField(default="127.0.0.1")
    port     = models.IntegerField(default=3333)
    enable_register = models.BooleanField(default=True)


"""
    my house model
"""
class Device(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField(default='')
    location = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()            

class Home(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = UPLOAD_ROOT_HOUSR_PLAN)

SENSORCHOICE = (
 ('s', 'switch'),
 ('n', 'numeric'),
 ('p', 'picture'),
)
CONDITIONCHOICE = (
 ('lt', 'less than'),
 ('lte', 'less than or equal'),
 ('gt', 'greater than'),
 ('gte', 'greater than or equal'),
 ('ne', 'not equal'),
 ('e', 'equal'),
)
class Sensor(models.Model):
    device = models.ForeignKey(Device, related_name="sensor")  #books = author.books.all()
    name = models.CharField(max_length=100)
    describe = models.TextField(default='')
    sensor_class = models.CharField(max_length=1, choices=SENSORCHOICE)    
    unit = models.CharField(max_length=20, blank=True)
    callback_value = models.FloatField(default=0)
    callback_condition = models.CharField(max_length=3, blank=True, choices=CONDITIONCHOICE)
    callback_file = models.CharField(max_length=120, blank=True)


class SwitchDatapoint(models.Model):    
    sensor = models.ForeignKey(Sensor, unique=True)  
    status = models.BooleanField(default=False)
class NumDatapoint(models.Model):  
    sensor = models.ForeignKey(Sensor)  
    #yyyy-MM-dd HH:mm:ss
    key = models.DateTimeField(unique=True)
    value = models.FloatField()   
class PicDatapoint(models.Model):  
    sensor = models.ForeignKey(Sensor)  
    #yyyy-MM-dd HH:mm:ss
    key = models.DateTimeField(unique=True)
    pic_file = models.ImageField(upload_to = UPLOAD_ROOT_PIC) 


"""
    others
"""
TYPECHOICE = (
 ('d', 'danger'),
 ('i', 'info'),
 ('w', 'warning'),
)

class Notification(models.Model):
    """消息通知类
    """
    type = models.CharField(max_length=1, choices=TYPECHOICE)
    ## 0 for all
    user_id = models.IntegerField(db_index=True, default=0)
    title = models.TextField(default='')
    content = models.TextField(default='')
    has_readed = models.BooleanField(default=False)