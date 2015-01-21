#coding=utf-8
from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  

import os
import json as simplejson    

from forms import *
from models import *
from common import client
from common import globaldata
from common import utils


# def requires_login(view):
#     def new_view(request, *args, **kwargs):
#         return view(request, *args, **kwargs)                       
#     return new_view          
# globaldata.getLogger().debug("avail space" + str(avail));                                             
global AppList

@login_required  
def dashboard(request, title='dashboard', belong=None):
    pisettings_instance = globaldata.getclient()
    user_count = PiUser.objects.count()   
    if(client.socket_test(pisettings_instance.ip,  pisettings_instance.port)):
        connection = "True"
        connection = "False"
    if globaldata.NasEnable:
        nas_enable = 'Enable'
    else:
        nas_enable = 'Disable'
    app_num = len(globaldata.AppList)

    #logfile
    pihome_log_file = open(globaldata.cwd + '/log/pihome.log', 'r')
    pihome_log_lines = pihome_log_file.readlines()
    pihome_log = utils.lineslimit(pihome_log_lines, 300)
    cpp_log_file = open(globaldata.cwd + '/log/pihome.log', 'r')
    cpp_log_lines = cpp_log_file.readlines()
    cpp_log = utils.lineslimit(cpp_log_lines, 300)

    t = get_template('dashboard/dashboard.html')
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
def settings_account_view(request, title='account', belong={'settings'}):
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
def settings_general_view(request, title='general', belong={'settings'}):
    pisettings_instance = globaldata.getclient()
    form = PiSettingsForm(request.POST or None, instance = pisettings_instance)
    if form.is_valid():
        form.save()
        # form = PiSettingsForm(instance = pisettings_instance)
    t = get_template('settings/general.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def status_about_view(request, title='about', belong={'status'}):
    t = get_template('status/about.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  status_default_view(request, title='default', belong={'status'}):
    pisettings_instance = globaldata.getclient()

    message = { "title" : "status"}
    message['cmd'] = 'get';

    pi_ret = client.socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)

    t = get_template('status/default.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  status_dmesg_view(request, title='kernel log', belong={'status'}):
    dmesg = os.popen("dmesg")
    log = dmesg.read()   
    t = get_template('status/dmesg.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_video_view(request, title='video', belong={'nas'}):
    minidlna_url = request.get_host()
    minidlna_url = minidlna_url[ :minidlna_url.find(':')]+ ':8200'

    t = get_template('nas/video.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_download_view(request, title='download', belong={'nas'}):
    t = get_template('nas/download.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  nas_file_view(request, title='filebrowser', belong={'nas'}):
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
def  add_device_view(request, title='add device', belong={'home'}):
    try:
        home_instance = Home.objects.get(id =1)
        img_url = '/media/' + str(home_instance.img)
    except:
        return HttpResponseRedirect('/PiApp/home/index/')
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
    t = get_template('home/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  manage_device_view(request, title='manage', belong={'home'}):
    device_all = Device.objects.all()    
    t = get_template('home/manage.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  add_home_view(request, title='add home', belong={'home'}):
    try:
        home_instance = Home.objects.get(id =1)
        form = HomeForm(request.POST or None, request.FILES, instance = home_instance)    
        home_exist = True       
    except:
        form = HomeForm(request.POST or None, request.FILES)
        home_exist = False     
    if request.method != 'POST' and home_exist == True:
        form = HomeForm(None, instance = home_instance)
    if form.is_valid():
        home = form.save()  
    if home_exist:
        img_url = '/media/' + str(home_instance.img)
    else:
        img_url = '/static/img/house_plan.jpg'
    HomeForm(instance = home_instance)
    t = get_template('home/add_home.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  home_view(request, title='home', belong=None):
    try:
        home_instance = Home.objects.get(id =1)
        img_url = '/media/' + str(home_instance.img)
        home_exist = True
    except:
        home_exist = False
    t = get_template('home/home.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  edit_device_view(request, title='edit device', belong={'home'}):
    try:
        home_instance = Home.objects.get(id =1)
        img_url = '/media/' + str(home_instance.img)
    except:
        return HttpResponseRedirect('/PiApp/home/index/')

    device_id = request.GET['id']
    device_instance = Device.objects.get(id =device_id)
    form = DeviceForm(request.POST or None, instance= device_instance)

    if form.is_valid():
        form.save()
    t = get_template('home/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required 
def  add_sensor_view(request, title='add sensor', belong={'home'}):
    device_id = request.GET['id']
    t = get_template('home/add_sensor.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


#######################################
##               user               ###
#######################################
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

