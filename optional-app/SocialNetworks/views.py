#coding=utf-8
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required 
import json as simplejson 

from common import globaldata

from models import *

cwd  = globaldata.cwd + '/App/SocialNetworks/'

try:
    pisettings_instance = sns_test.objects.get(id =1)
except:
    pisettings_instance = sns_test.objects.create(id =1) 

@login_required  
def index(request):
    t = get_template('SocialNetworks/index.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))