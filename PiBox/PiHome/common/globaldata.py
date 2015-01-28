#coding=utf-8
'''
# This modules contains shared data

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

import os,sys,logging

from PiApp.models import PiSettings

import struct.pci_list
import struct.app_ini

VERSION = '0.3.0'

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
APP_DIR  = BASE_DIR + '/App'

#pihome control interface list,will be used to create sidebar and titlebar 
pci_list = struct.pci_list.PciList()
#app info read from ini
app_ini = struct.app_ini.AppIni(APP_DIR)

#others
def getclient():
    try:
        pisettings_instance = PiSettings.objects.get(id =1)
    except:
        pisettings_instance = PiSettings.objects.create(id =1) 

    return pisettings_instance


def getLogger():
    logger = logging.getLogger('pihome')
    return logger






