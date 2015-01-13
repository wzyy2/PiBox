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
from django.utils import simplejson  

from forms import *
from models import *
from app import *
from utils import *
import gl

def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():                        #如果用户没有登录，跳转到登录界面
            return HttpResponseRedirect('/accounts/login/')
        return view(request, *args, **kwargs)                          #否则返回传进来的方法
    return new_view                                                    #返回new_view值：登录视图或者是传进来的视图

def dashboard(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

    user_count = PiUser.objects.count()   

    if(socket_test(pisettings_instance.ip,  pisettings_instance.port)):
        connection = "TRUE"
    else:
        connection = "FALSE"

    nas_enable = gl.nas_enable
    app_num = gl.app_num()

    t = get_template('dashboard/dashboard.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def login_view(request): 
    if request.user.is_authenticated():
        return HttpResponseRedirect("/PiApp/dashboard/")             
    if request.method != 'POST':  
        t = get_template('login.html')
        c = RequestContext(request,locals())   
        return HttpResponse(t.render(c))    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)   
        ret = 'Ok'
    else:
        ret = 'Fail'
    t = get_template('register_return.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))      

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/PiApp/dashboard/")  

def register_view(request):  
    ''''' 
        功能：往数据库中添加一条用户注册信息 
    '''  
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

def fzf_view(request):
    t = get_template('404.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def fzz_view(request):
    t = get_template('500.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def settings_account_view(request):
    if request.user.is_authenticated():
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
    else:
        t = get_template('login.html')
        c = RequestContext(request,locals())   
    return HttpResponse(t.render(c))

def settings_general_view(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)
    form = PiSettingsForm(request.POST or None, instance = pisettings_instance)
    if form.is_valid():
        form.save()
        form = PiSettingsForm(instance = pisettings_instance)
    t = get_template('settings/general.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def status_server_view(request):
    t = get_template('status/server.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def  status_piclient_view(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

    message = { "title" : "status"}
    message['cmd'] = 'get';

    pi_ret = socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)

    t = get_template('status/client.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def  nas_file_view(request):
    t = get_template('nas/file.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def  nas_video_view(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

    minidlna_url = request.get_host()
    minidlna_url = minidlna_url[ :minidlna_url.find(':')]+ ':8200'

    t = get_template('nas/video.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def  nas_download_view(request):
    t = get_template('nas/download.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def nas_minidlna_view(request):
    t = get_template('500.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def webssh_view(request):
    ssh_url = request.get_host()
    ssh_url = ssh_url[ :ssh_url.find(':')]+ ':8001'

    t = get_template('webssh/webssh.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))