from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *



urlpatterns = patterns('',
    (r'^$', dashboard),
    (r'^dashboard/$', dashboard),

    (r'^settings/account/$', settings_account_view),
    (r'^settings/general/$', settings_general_view),

    (r'^status/default/$', status_default_view),
    (r'^status/about/$', status_about_view),
    (r'^status/dmesg/$', status_dmesg_view),
    (r'^status/process/$', status_process_view),

    (r'^nas/file/$', nas_file_view),
    (r'^nas/video/$', nas_video_view),
    (r'^nas/download/$', nas_download_view),

    (r'^webssh/$', webssh_view), 

    (r'^home/index/$', home_view),   
    (r'^home/help/$', home_help_view),   
    (r'^home/add_home/$', add_home_view),
    (r'^home/device/$', device_view), 
    (r'^home/add_device/$', add_device_view),  
    (r'^home/edit_device/$', edit_device_view),  
    (r'^home/manage_device/$', manage_device_view),  
    (r'^home/add_sensor/$', add_sensor_view),  
    (r'^home/edit_sensor/$', edit_sensor_view), 
)

