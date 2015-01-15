from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from filemanager import path_end
from views import *

urlpatterns = patterns('',
    (r''+path_end, index),
)
