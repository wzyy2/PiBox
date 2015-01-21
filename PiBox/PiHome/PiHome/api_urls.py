from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

#API

urlpatterns = patterns('',
    (r'accounts/check/username', check_username),
    (r'accounts/login', login_api),
    (r'accounts/logout', logout_api),
    (r'accounts/register', register_api),
    (r'accounts/info', account_info_api),
    (r'accounts/change', account_change_api),
    (r'accounts/check/login', check_login),
    (r'PiApp/dashboard', dashboard_api),
    (r'PiApp/status/client', piclient_api),
    (r'PiApp/nas', nas_api),
    (r'PiApp/server', server_api),    

    (r'PiApp/settings/account', settings_account_api),    
    (r'PiApp/settings/general', settings_general_api),   


    (r'home/device', device_json),     
    (r'home/device/remove', remove_device_json),      
)