#coding=utf-8
import re
import sys
import os
from common import globaldata


def app_info(request):

    info = []
    for item in globaldata.AppList:
        info.append(item.name);
    return  {
        'APPINFO': info,
    }

def version(request):
    return  {
        'VERSION': globaldata.VERSION,
    }
