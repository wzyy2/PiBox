from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *

urlpatterns = patterns('',
    (r'^$', index),
)
