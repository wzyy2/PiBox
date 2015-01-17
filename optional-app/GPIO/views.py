#coding=utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required  
import json as simplejson

from PiApp.forms import *
from PiApp.models import *

from common import client
from common import globaldata
from common import utils

pisettings_instance = globaldata.getclient()

@login_required  
def GPIO(request):
    message = { "title" : "application", "app_name" : "GPIO", "action" : "read_info"}
    try:
        pi_ret = socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))  

    t = get_template('GPIO/gpio.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def  GPIO_API(request):
    message = { "title" : "application", "app_name" : "GPIO"}
    try:
        if request.method == 'GET':
            message['action'] = request.GET['action'] ;
            message['pin_num'] =  int(request.GET['pin_num'] );
            pi_ret = socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))  

    pin_num = 0
    
    return HttpResponse(simplejson.dumps(pi_ret.message))  


#mode
#define INPUT            0
#define OUTPUT           1
#define PWM_OUTPUT       2
#define GPIO_CLOCK       3
#PUD
#define PUD_OFF          0
#define PUD_DOWN         1
#define PUD_UP           2
#PWM
#define PWM_MODE_MS     0
#define PWM_MODE_BAL        1