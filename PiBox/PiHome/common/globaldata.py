#coding=utf-8
import os,sys,logging
from PiApp.forms import *
from PiApp.models import *

VERSION = '0.2.2'
    
NasEnable="ENABLE"

#app info
class Appstruct():
    name = None

AppList = list()

#register app list
cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
appcwd  = cwd + '/App'
list = os.listdir(appcwd)
info = []
for item in list:
    if os.path.isdir(os.path.join(appcwd, item)):
        app = Appstruct()
        app.name = item
        AppList.append(app)


def getclient():
    try:
        pisettings_instance = PiSettings.objects.get(id =1)
    except:
        pisettings_instance = PiSettings.objects.create(id =1) 

    return pisettings_instance


def getLogger():
    logger = logging.getLogger('pihome')
    return logger