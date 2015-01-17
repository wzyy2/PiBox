from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import *
#/PiApp/application

urlpatterns = patterns('',
    (r'^$', GPIO),
    (r'GPIO_API', GPIO_API),
)
