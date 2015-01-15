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
import json as simplejson 


@login_required 
def  index(request):
    t = get_template('nas/file.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))