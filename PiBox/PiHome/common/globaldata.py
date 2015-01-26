#coding=utf-8
import os,sys,logging
from PiApp.forms import *
from PiApp.models import *
import pci_list

VERSION = '0.3.0'

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
APP_DIR  = BASE_DIR + '/App'

#pihome control interface list,will be used to create sidebar and titlebar 
pci_list = pci_list.PciList()

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






