from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from PiApp.views import *
from PiApp.api import *

from views import *
#/PiApp/application

urlpatterns = patterns('',
    (r'^$', index),
    (r'^open/', open_camera),    
    (r'^close/', close_camera),    
    (r'^temp.jpg', image),    
)
