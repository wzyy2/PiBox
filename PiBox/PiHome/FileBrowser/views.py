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

def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():                        #如果用户没有登录，跳转到登录界面
            return HttpResponseRedirect('/accounts/login/')
        return view(request, *args, **kwargs)                          #否则返回传进来的方法
    return new_view                                                    #返回new_view值：登录视图或者是传进来的视图

def  index(request):
    t = get_template('nas/file.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))