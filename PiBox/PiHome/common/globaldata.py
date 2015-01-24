#coding=utf-8
import os,sys,logging
from PiApp.forms import *
from PiApp.models import *

VERSION = '0.3.0'
NasEnable=True

######################################################
#app info
class Appstruct():
    name = None

AppList = list()
#register app list
cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
APP_DIR  = cwd + '/App'
list = os.listdir(APP_DIR)
info = []
for item in list:
    if os.path.isdir(os.path.join(APP_DIR, item)):
        app = Appstruct()
        app.name = item
        AppList.append(app)

###################################################
def getclient():
    try:
        pisettings_instance = PiSettings.objects.get(id =1)
    except:
        pisettings_instance = PiSettings.objects.create(id =1) 

    return pisettings_instance


def getLogger():
    logger = logging.getLogger('pihome')
    return logger






