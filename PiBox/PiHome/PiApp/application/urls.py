from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

from filebrowser.sites import site
import os
import sys

urlpatterns = patterns('',)

cwd  = os.getcwd() + '/App'
list = os.listdir(cwd)
sys.path.append(cwd);

for item in list:
    if os.path.isdir(os.path.join(cwd, item)):
        urlpatterns += patterns ('',
            (r'^' + item + '/', include(item + '.django.urls')),
            )