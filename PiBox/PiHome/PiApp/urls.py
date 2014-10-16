from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *
from api import *

urlpatterns = patterns('',
    (r'^$', dashboard),
    (r'dashboard/$', dashboard),
    (r'settings/account/$', settings_account_view),
    (r'settings/general/$', settings_general_view),
    (r'status/server/$', status_server_view),
    (r'status/piclient/$', status_piclient_view),
    (r'nas/file/$', nas_file_view),
    (r'nas/video/$', nas_video_view),
    (r'nas/download/$', nas_download_view),
    (r'nas/minidlna/$', nas_minidlna_view),  
)

urlpatterns += patterns ('',
    (r'^application/', include('PiApp.application.urls')),
)