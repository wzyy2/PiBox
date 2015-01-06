from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from PiApp.views import *
from PiApp.api import *

from views import *
#/API/application/GPIO/

urlpatterns = patterns('',
    (r'GPIO_API', GPIO_API),
)
