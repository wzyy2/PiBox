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

from PiApp.forms import *
from PiApp.models import *
from PiApp.app import *
from PiApp.utils import *
import PiApp.gl

import v4l2capture
from PIL import Image 
import select

try:
   pisettings_instance = PiSettings.objects.get(id =1)
except:
   pisettings_instance = PiSettings.objects.create(id =1)

html_source_header = "application/webcam/"



def index(request):
    t = get_template(html_source_header + 'django/html/webcam.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def image(request):
    video = v4l2capture.Video_device("/dev/video0")
    size_x, size_y = video.set_format(1280, 1024)
    video.create_buffers(1)
    video.queue_all_buffers()
    video.start()
    select.select((video,), (), ())
    image_data = video.read()
    video.close()
    http = HttpResponse(mimetype='image/jpeg')
    # img = Image.open('/home/ubuntu/PiBox/App/webcam/django/static/img/pi_logo.png')
    # img.save(http,'png')
    img = Image.fromstring("RGB", (size_x, size_y), image_data)
    img.save(http,'jpg')
    return http

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