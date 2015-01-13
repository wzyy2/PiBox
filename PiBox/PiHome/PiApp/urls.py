from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *
from api import *

urlpatterns = patterns('',
    (r'^$', dashboard),
    (r'dashboard/$', dashboard),
    (r'settings/account/$', settings_account_view),
    (r'settings/general/$', settings_general_view),
    (r'status/about/$', status_about_view),
    (r'status/default/$', status_default_view),
    (r'status/dmesg/$', status_dmesg_view),
    (r'nas/video/$', nas_video_view),
    (r'nas/download/$', nas_download_view),
    (r'webssh/$', requires_login(webssh_view)),  
)

urlpatterns += patterns ('',
    (r'^application/', include('PiApp.application.urls')),
)