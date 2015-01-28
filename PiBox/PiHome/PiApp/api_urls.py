#coding=utf-8
'''
# The code in this file will modify api url which used to ret json data

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

'''
    api url
'''
urlpatterns = patterns('',
    (r'^accounts/check/username/$', check_username),
    (r'^accounts/login/$', login_api),
    (r'^accounts/logout/$', logout_api),
    (r'^accounts/register/$', register_api),
    (r'^accounts/info/$', account_info_api),
    (r'^accounts/change/$', account_change_api),
    (r'^accounts/check/login/$', check_login),
    (r'^PiApp/dashboard/$', dashboard_api),
    (r'^PiApp/status/client/$', piclient_api),
    (r'^PiApp/status/process/kill/$', kill_process_api),
    (r'^PiApp/nas/$', nas_api),
    (r'^PiApp/server/$', server_api),    

    (r'^PiApp/settings/account/$', settings_account_api),    
    (r'^PiApp/settings/general/$', settings_general_api),   

    (r'^PiApp/notification/delete/$', delete_notification_api), 


# .+
    (r'^device/(?P<device_id>\d*)/$', get_device_by_id_json),     
    (r'^device/(?P<device_id>\d*)/remove/$', remove_device_by_id_json),    
    (r'^device/(?P<device_id>\d*)/sensor/$', get_sensor_by_device_id_json),  
    
    (r'^sensor/(?P<sensor_id>\d*)/$', get_sensor_by_sensor_id_json),  
    
    (r'^sensor/(?P<sensor_id>\d*)/remove/$', remove_sensor_by_id_json), 
    (r'^sensor/(?P<sensor_id>\d*)/add_callback/$', add_sensor_callback_json), 
    (r'^sensor/(?P<sensor_id>\d*)/get_callback/$', get_sensor_callback_json), 

    ## API for user!
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/$', new_datapoint_json), 
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/edit/$', edit_datapoint_json), 
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/get/$', get_datapoint_json),  
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/remove/$', remove_datapoint_json),  
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/history/$', history_datapoint_json),  
    (r'^sensor/(?P<sensor_id>\d*)/datapoint/key_range/$', key_range_datapoint_json),      
)