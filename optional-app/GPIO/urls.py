from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import *


urlpatterns = patterns('',
    (r'^$', GPIO), 
    (r'^add/', add), 
    (r'^remove/', remove), 
    (r'^read_direction/', read_direction), 
    (r'^write_direction/', write_direction), 
    (r'^read_value/', read_value), 
    (r'^write_value/', write_value), 
    (r'^exported_gpio/', exported_gpio), 
)
