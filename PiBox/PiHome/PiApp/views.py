#coding=utf-8
'''
# PiApp's view here!
# The view that return json data is in api.py

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  

import os
import json as simplejson    

from PiHome import settings
from PiApp.forms import *
from PiApp.models import *
from common.api import client, notification
from common import globaldata
from common import utils



@login_required  
def dashboard(request, title='dashboard', belong=None):
    pisettings_instance = globaldata.getclient()
    user_count = PiUser.objects.count()   
    device_count = Device.objects.count()   
    if(client.socket_test(pisettings_instance.ip,  pisettings_instance.port)):
        connection = "True"
    else:
        connection = "False"

    applist = globaldata.pci_list.applist()
    app_num = len(applist)
    media_root = settings.MEDIA_ROOT
    DEVICE = Device.objects.all()
    try:
        home_instance = Home.objects.get(id =1)
        home_exist = True
    except:
        home_exist = False

    #logfile
    pihome_log_file = open(globaldata.BASE_DIR + '/log/pihome.log', 'r')
    pihome_log_lines = pihome_log_file.readlines()
    pihome_log = utils.lineslimit(pihome_log_lines, 100)
    cpp_log_file = open(globaldata.BASE_DIR + '/log/pihome.log', 'r')
    cpp_log_lines = cpp_log_file.readlines()
    cpp_log = utils.lineslimit(cpp_log_lines, 100)

    t = get_template('dashboard/dashboard.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required  
def notification_view(request, title='notification', belong=None):
    others = notification.get_all(request.user.id)

    unread = notification.get_unread_clear(request.user.id)
   
    t = get_template('notification.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def fzf_view(request, title='404', belong=None):
    t = get_template('404.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def fzz_view(request, title='500', belong=None):
    t = get_template('500.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def settings_account_view(request, title='account', belong=['settings']):
    user = PiUser.objects.get(username = request.user.username)
    form = PiAccountForm(request.POST or None, instance = user)
    if form.is_valid():
        user.first_name=form.cleaned_data['first_name']
        user.last_name=form.cleaned_data['last_name'] 
        if(form.cleaned_data['password1']  !=  ""):   
            password=form.cleaned_data['password1']
            if password != None:
                user.set_password(password)
        user.save()
    t = get_template('settings/account.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def settings_general_view(request, title='general', belong=['settings']):
    pisettings_instance = globaldata.getclient()
    form = PiSettingsForm(request.POST or None, instance = pisettings_instance)
    if form.is_valid():
        form.save()
        # form = PiSettingsForm(instance = pisettings_instance)
    t = get_template('settings/general.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def status_process_view(request, title='process', belong=['status']):
    info = os.popen('ps aux').readlines()
    i = 0
    process_info = list()
    for line in info :
        i += 1
        if i > 1:
            get = line.split()
            a = dict()
            a['pid'] = get[1]
            a['owner'] = get[0]
            a['command'] = get[10]
            for item in get[11:]:
                a['command'] += ' ' + item
            a['cpu'] = get[2]
            a['memory'] = get[3]  
            process_info.append(a) 
    t = get_template('status/process.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def status_about_view(request, title='about', belong=['status']):                                             
    t = get_template('status/about.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  status_default_view(request, title='default', belong=['status']):
    pisettings_instance = globaldata.getclient()

    message = { "title" : "status"}
    message['cmd'] = 'get';

    pi_ret = client.socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)

    t = get_template('status/default.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  status_dmesg_view(request, title='kernel log', belong=['status']):
    dmesg = os.popen("dmesg")
    log = dmesg.read()   
    t = get_template('status/dmesg.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_video_view(request, title='video', belong=['nas']):
    minidlna_url = request.get_host()
    minidlna_url = minidlna_url[ :minidlna_url.find(':')]+ ':8200'

    t = get_template('nas/video.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_download_view(request, title='download', belong=['nas']):
    t = get_template('nas/download.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_file_view(request, title='filebrowser', belong=['nas']):
    t = get_template('nas/file.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  webssh_view(request, title='webssh', belong=None):
    ssh_url = request.get_host()
    ssh_url = ssh_url[ :ssh_url.find(':')]+ ':8001'

    t = get_template('webssh/webssh.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  home_view(request, title='my house', belong=None):
    try:
        home_instance = Home.objects.get(id = 1)
        img_url = '/media/' + str(home_instance.img)
        home_exist = True
        device_all = Device.objects.all()  
    except:
        home_exist = False
    t = get_template('home/home.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  add_home_view(request, title='add home', belong=['my house']):
    try:
        home_instance = Home.objects.get(id =1)
        form = HomeForm(request.POST or None, request.FILES, instance = home_instance)    
        home_exist = True       
    except:
        form = HomeForm(request.POST or None, request.FILES)
        home_exist = False   

    if request.method != 'POST' and home_exist == True:
        form = HomeForm(None, instance = home_instance)
    elif request.method != 'POST' and home_exist == False:
        form = HomeForm(None)

    if form.is_valid():
        home = form.save()  

    if home_exist:
        img_url = '/media/' + str(home_instance.img)
    else:
        img_url = '/static/img/house_plan.jpg'
   
    t = get_template('home/add_home.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  home_help_view(request, title='document', belong=['my house']):
    t = get_template('home/help.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def  home_help_en_view(request, title='document-en', belong=['my house']):
    t = get_template('home/help_en.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  device_view(request):
    device_id = request.GET['device_id']
    device_instance = Device.objects.get(id = device_id)
    sensors = device_instance.sensor.all()   

    t = get_template('home/device.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  add_device_view(request, title='add device', belong=['my house']):
    try:
        home_instance = Home.objects.get(id =1)
        img_url = '/media/' + str(home_instance.img)
    except:
        return HttpResponseRedirect('/PiApp/home/index/')
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/PiApp/home/manage_device/')
    t = get_template('home/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  manage_device_view(request, title='manage', belong=['my house']):
    device_all = Device.objects.all()    
    count = Device.objects.count()   
    t = get_template('home/manage.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  edit_device_view(request, title='edit device', belong=['my house', 'manage']):
    try:
        home_instance = Home.objects.get(id = 1)
        img_url = '/media/' + str(home_instance.img)
    except:
        return HttpResponseRedirect('/PiApp/home/index/')

    device_id = request.GET['device_id']
    device_instance = Device.objects.get(id = device_id)
    form = DeviceForm(request.POST or None, instance = device_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/PiApp/home/manage_device/')

    t = get_template('home/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  add_sensor_view(request, title='add sensor', belong=['my house', 'manage']):
    device_id = request.GET['device_id']
    get_device = Device.objects.get(id = device_id)
    form = SensorForm(request.POST or None)
    # Sensor.objects.create(name="11",describe="111", sensor_class="s", device = get_device)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.device = get_device
        sensor.save()
        return HttpResponseRedirect('/PiApp/home/manage_device/')

    t = get_template('home/add_sensor.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  edit_sensor_view(request, title='edit sensor', belong=['my house', 'manage']):
    sensor_id = request.GET['sensor_id']
    get_sensor = Sensor.objects.get(id = sensor_id)
    form = SensorForm(request.POST or None, instance = get_sensor)
    # Sensor.objects.create(name="11",describe="111", sensor_class="s", device = get_device)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.save()
        return HttpResponseRedirect('/PiApp/home/manage_device/')

    t = get_template('home/edit_sensor.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  sensor_data_view(request, title='sensor data', belong=['my house', 'manage']):
    sensor_id = request.GET['sensor_id']
    get_sensor = Sensor.objects.get(id = sensor_id)

    if get_sensor.sensor_class == 'n':
        datapoint = NumDatapoint.objects.filter(sensor = get_sensor)
    elif get_sensor.sensor_class == 'p': 
        datapoint = PicDatapoint.objects.filter(sensor = get_sensor)

    domain = request.get_host() + settings.MEDIA_URL
    t = get_template('home/sensor_data.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
'''
 user admin
'''
def login_view(request): 
    if request.user.is_authenticated():
        return HttpResponseRedirect("/PiApp/dashboard/")             
    if request.method != 'POST': 
        try: 
            next_url = request.GET['next']
        except:
            next_url = ''
        t = get_template('login.html')
        c = RequestContext(request,locals())   
        return HttpResponse(t.render(c))    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)   
        ret = {'msg':'ok'}
    else:
        ret = {'msg':'fail'}
    return HttpResponse(simplejson.dumps(ret))      

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/PiApp/dashboard/")  

def register_view(request):  
    pisettings_instance = globaldata.getclient()
    if pisettings_instance.enable_register != True:
        return HttpResponse("You are not be allowed to register") 
    form = PiRegisterForm(request.POST or None)
    if form.is_valid():
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']      
        email = form.cleaned_data['email'] 
        password=form.cleaned_data['password1']        
        try:
            user = PiUser.objects.create_user(email, email, password)    
            if user is not None:  
                user.first_name =  first_name
                user.last_name = last_name
                user.is_staff = True  
                user.save()  
                user = authenticate(username=email, password=password)
                login(request, user)    
                ret = 'Ok'
                t = get_template('register_return.html')
                c = RequestContext(request,locals())
                return HttpResponse(t.render(c))
        except:  
            ret = 'Fail'
            t = get_template('register_return.html')
            c = RequestContext(request,locals())
            return HttpResponse(t.render(c))
    else:
        t = get_template('register.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))  


# def requires_login(view):
#     def new_view(request, *args, **kwargs):
#         return view(request, *args, **kwargs)                       
#     return new_view          
# globaldata.getLogger().debug("avail space" + str(avail));                                             
