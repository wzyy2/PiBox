#coding=utf-8
import os

VERSION = '0.2.0'
    
nas_enable="ENABLE"

def app_num():

    cwd  = os.getcwd() + '/App'
    list = os.listdir(cwd)
    sum = 0

    for item in list:
        if os.path.isdir(os.path.join(cwd, item)):
            sum = sum + 1

    return sum