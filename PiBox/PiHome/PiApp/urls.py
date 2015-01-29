#coding=utf-8
'''
# The code in this file will modify url and register pci list

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *
from common import globaldata
import sys,os

'''
    default display url
'''
urlpatterns = patterns('',)

cwd  = globaldata.APP_DIR
list = os.listdir(cwd)
sys.path.append(cwd);
for item in list:
    if os.path.isdir(os.path.join(cwd, item)):
        urlpatterns += patterns ('',
            (r'^app/' + item + '/', include(item + '.urls')),
            )

urlpatterns += patterns('',
    (r'^$', dashboard),
    (r'^dashboard/$', dashboard),
    (r'^notification/$', notification_view),

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
    (r'^home/help/en$', home_help_en_view),
    (r'^home/add_home/$', add_home_view),
    (r'^home/device/$', device_view), 
    (r'^home/add_device/$', add_device_view),  
    (r'^home/edit_device/$', edit_device_view),  
    (r'^home/manage_device/$', manage_device_view),  
    (r'^home/add_sensor/$', add_sensor_view),  
    (r'^home/edit_sensor/$', edit_sensor_view), 
    (r'^home/sensor_data/$', sensor_data_view), 
)


'''
    register pihome control interface list,will be used to create sidebar and titlebar 
'''    
pci_list = globaldata.pci_list
#register dashboard to pci list
pci_list.register('dashboard', "/PiApp/dashboard/", 'fa-dashboard')

#register App list to pci list
pci_list.register('application', '', 'fa-folder')
list = os.listdir(globaldata.APP_DIR)
for item in list:
    if os.path.isdir(os.path.join(globaldata.APP_DIR, item)):
        name = globaldata.app_ini.read(item, 'Name')
        pci_list.addchild(name, "/PiApp/app/" + item, 'application')


pci_list.register('my house', "/PiApp/home/index/", 'fa-home')        
pci_list.addchild('home', "/PiApp/home/index/", 'my house')
pci_list.addchild('add device', "/PiApp/home/add_device/", 'my house')
pci_list.addchild('manage device', "/PiApp/home/manage_device/", 'my house')
pci_list.addchild('document', "/PiApp/home/help/", 'my house')

pci_list.register('nas', "/PiApp/nas/file/", 'fa-hdd-o')       
pci_list.addchild('fileBrowser', "/PiApp/nas/file/", 'nas')
pci_list.addchild('download', "/PiApp/nas/download/", 'nas')

pci_list.register('SSH', "/PiApp/webssh/", 'fa-laptop')       

pci_list.register('status', "/PiApp/status/default/", 'fa-bar-chart-o')       
pci_list.addchild('default', "/PiApp/status/default/", 'status')
pci_list.addchild('kernel log', "/PiApp/status/dmesg/", 'status')
pci_list.addchild('process', "/PiApp/status/process/", 'status')
pci_list.addchild('about', "/PiApp/status/about/", 'status')

pci_list.register('settings', "/PiApp/settings/general/", 'fa-cog')       
pci_list.addchild('general', "/PiApp/settings/general/", 'settings')
pci_list.addchild('account', "/PiApp/settings/account/", 'settings')

   