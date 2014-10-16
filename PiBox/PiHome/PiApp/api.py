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


from models import *
from utils import *
from app import *
from forms import *
import gl


def login_api(request):           
    if request.method == 'POST':  
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)  
            ret = {'msg':'ok'}    
            ret['firstname'] = user.first_name
            ret['lastname'] = user.last_name
            return HttpResponse(simplejson.dumps(ret))   
        else:
            return HttpResponse(simplejson.dumps({'msg':'fail'}))   

def logout_api(request):
    logout(request)
    return HttpResponse(simplejson.dumps({'msg':'ok'}))   

def check_username(request):  
    if request.method == 'GET':  
        try:  
            if utils.validateEmail(request.GET['username'])  == 0:
                return HttpResponse(simplejson.dumps({'msg':'请输入正确邮箱格式'}))  
            user = PiUser.objects.get(username = request.GET['username'])
            if user is not None:  
                return HttpResponse(simplejson.dumps({'msg':'用户名已存在'}))  
        except:  
            return HttpResponse(simplejson.dumps({'msg':'用户名可以使用'}))  

def check_login(request):  
    if request.user.is_authenticated():
        return HttpResponse(simplejson.dumps({'msg':'ok'}))  
    else:
        return HttpResponse(simplejson.dumps({'msg':'fail'}))  


def register_api(request):  
    ''''' 
        功能：往数据库中添加一条用户注册信息 
    '''  
    form = PiRegisterForm(request.POST or None)
    if form.is_valid():
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']      
        email = form.cleaned_data['email'] 
        password=form.cleaned_data['password1']
        user = PiUser.objects.create_user(email, email, password)    
        if user is not None:  
            user.first_name =  first_name
            user.last_name = last_name
            user.is_staff = True  
            user.save()  
            return HttpResponse(simplejson.dumps({'msg':'ok'}))  
        else:  
            return HttpResponse(simplejson.dumps({'msg':'fail'}))  

def account_change_api(request):
    if request.user.is_authenticated():
        user = PiUser.objects.get(username = request.user.username)
        form = PiAccountForm(request.POST or None, instance = user)
        if form.is_valid():
            user.first_name=form.cleaned_data['firstname']
            user.last_name=form.cleaned_data['lastname']      
            if(form.cleaned_data['password1']  !=  "") :  
                password=form.cleaned_data['password1']
                if password != None:
                    user.set_password(password)
            user.save()
            return HttpResponse(simplejson.dumps({'msg':'ok'}))  
    return HttpResponse(simplejson.dumps({'msg':'fail'}))  

def account_info_api(request):
    if request.user.is_authenticated():
        user = PiUser.objects.get(username = request.user.username)
        ret = {'msg':'ok'}
        ret[firstname] = user.first_name
        ret[lastname] = user.last_name
        return HttpResponse(simplejson.dumps({'msg':'ok'}))  
    return HttpResponse(simplejson.dumps({'msg':'fail'}))  


def  piclient_api(request):
    try:
        pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

    message = { "title" : "status"}
    if request.method == 'GET':
        try:
            message['cmd'] =  request.GET['cmd'] ;
        except: 
            message['cmd'] =  '' ;

    pi_ret = socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)

    return HttpResponse(simplejson.dumps(pi_ret.message))  


def  nas_api(request):
    try:
        pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

      
    message = { "title" : "nas"}
    if request.method == 'GET':
        try:
            message['cmd'] =  request.GET['cmd'] ;
        except: 
            message['cmd'] =  '' ;

    pi_ret = socketjson_send_recv(pisettings_instance.ip,  pisettings_instance.port, message)

    return HttpResponse(simplejson.dumps(pi_ret.message))  

def  server_api(request):
    pi_ret = {'version':'0.10'}
    return HttpResponse(simplejson.dumps(pi_ret))


def  dashboard_api(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)

    pi_ret = {'nas': gl.nas_enable}
    if(socket_test(pisettings_instance.ip,  pisettings_instance.port)):
        pi_ret['connection'] = "TRUE"
    else:
        pi_ret['connection'] = "FALSE"
    pi_ret['app_num'] =   gl.app_num()
    pi_ret['user_count'] = PiUser.objects.count()

    return HttpResponse(simplejson.dumps(pi_ret))

def settings_account_api(request):
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
        t = get_template('settings/api_account.html')
        c = RequestContext(request,locals())
    else:
        t = get_template('login.html')
        c = RequestContext(request,locals())   
    return HttpResponse(t.render(c))

def settings_general_api(request):
    try:
       pisettings_instance = PiSettings.objects.get(id =1)
    except:
       pisettings_instance = PiSettings.objects.create(id =1)
    form = PiSettingsForm(request.POST or None, instance = pisettings_instance)
    if form.is_valid():
        form.save()
        form = PiSettingsForm(instance = pisettings_instance)
    t = get_template('settings/api_general.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))