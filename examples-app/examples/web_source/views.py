#coding=utf-8
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required 
import json as simplejson 


html_source_url = "application/examples/web_source/html/"
static_source_url = "static/examples/web_source/static/"
cwd  = globaldata.cwd + '/App/examples/'
