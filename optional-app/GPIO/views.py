#coding=utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required  
import json as simplejson

from PiApp.forms import *
from PiApp.models import *

from common.api import client
from common.driver import linux_gpio
from common import globaldata
from common import utils



gpio_dict = dict()

@login_required  
def GPIO(request, title='GPIO', belong=['application']):
    t = get_template('GPIO/gpio.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required  
def add(request):
    try:
        num = int(request.GET['num']) 
        gpio_dict[num] = linux_gpio.gpio(num)
        gpio_dict[num].gpio_export()
        if linux_gpio.gpio_exists(num) != True:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'})) 

@login_required  
def remove(request):
    try:
        num = int(request.GET['num']) 
        gpio_dict[num].gpio_unexport()
        if linux_gpio.gpio_exists(num) != False:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'})) 

@login_required  
def read_direction(request):
    try:
        num = int(request.GET['num']) 
        if linux_gpio.gpio_exists(num) != True:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        direction = gpio_dict[num].read_gpio_direction()
        return HttpResponse(simplejson.dumps({'msg':'ok', 'direction': direction}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'})) 

@login_required  
def read_value(request):
    try:
        num = int(request.GET['num']) 
        if linux_gpio.gpio_exists(num) != True:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        value = gpio_dict[num].read_gpio_value()
        return HttpResponse(simplejson.dumps({'msg':'ok', 'value':value}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))         

@login_required  
def write_direction(request):
    try:
        num = int(request.GET['num']) 
        direction = request.GET['direction']
        if linux_gpio.gpio_exists(num) != True:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        gpio_dict[num].write_gpio_direction(direction)
        return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'})) 

@login_required  
def write_value(request):
    try:
        num = int(request.GET['num']) 
        value = int(request.GET['value']) 
        if linux_gpio.gpio_exists(num) != True:
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
        gpio_dict[num].write_gpio_value(value)
        return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))         

@login_required  
def exported_gpio(request):
    ret = linux_gpio.scan_gpio()
    ret_num = list()
    for item in ret:
        num = int(item[4:])
        ret_num.append(num)
        gpio_dict[num] = linux_gpio.gpio(num)
    return HttpResponse(simplejson.dumps({'msg':'ok', 'exported_gpio': ret_num}))           
