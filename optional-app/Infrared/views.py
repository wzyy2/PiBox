#coding=utf-8
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required 
import json as simplejson 

from common import globaldata

cwd  = globaldata.cwd + '/App/Infrared/'

@login_required  
def index(request, title='Infrared', belong={'app'}):
    t = get_template('Infrared/index.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


