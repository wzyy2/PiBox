#coding=utf-8
import os,sys 
from PiApp.forms import *
from PiApp.models import *

import globaldata

#register app list
cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
callback_dir  = cwd + '/sh/callback'
callback_list = os.listdir(callback_dir)
# for item in callback_list:
#     if os.path.isdir(os.path.join(APP_DIR, item)):
#         app = Appstruct()
#         app.name = item
#         AppList.append(app)

def switch_callback(sensor, status):
    if sensor.callback_file in callback_list:
        read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name)  + ' ' + str(status)).read()
        globaldata.getLogger().debug(read);    

def num_callback(sensor, value, key):
    if sensor.callback_file in callback_list:
        if sensor.callback_condition == 'lt':
            if float(value) < sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name) + ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   
        elif sensor.callback_condition == 'lte':
            if float(value) <= sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name) + ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   
        elif sensor.callback_condition == 'gt':
            if float(value) > sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name)+ ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   
        elif sensor.callback_condition == 'gte':
            if float(value) >= sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name) + ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   
        elif sensor.callback_condition == 'ne':
            if float(value) != sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name) + ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   
        elif sensor.callback_condition == 'e':
            if float(value) == sensor.callback_value:
                read = os.popen('python ' + os.path.join(callback_dir, sensor.callback_file) + ' ' + str(sensor.name) + ' ' + str(value) + ' ' + str(key)).read()
                globaldata.getLogger().debug(read);   

         



