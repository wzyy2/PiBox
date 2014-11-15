#coding=utf-8
import re
import sys
import os



def app_info(request):

    cwd  = os.getcwd() + '/App'
    list = os.listdir(cwd)
    info = []
    for item in list:
        if os.path.isdir(os.path.join(cwd, item)):
            info.append(item);
    return  {
        'APPINFO': info,
    }
