from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

from filebrowser.sites import site
import os

#/PiApp/application

urlpatterns = patterns('',)

cwd  = os.getcwd() + '/PiHome/PiApp/application'
list = os.listdir(cwd)

for item in list:
    if os.path.isdir(os.path.join(cwd, item)):
            urlpatterns += patterns ('',
                (r'^' + item + '/', include('PiApp.application.' + item + '.urls')),
                )