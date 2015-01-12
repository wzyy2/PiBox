#coding=utf-8
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import simplejson  
from PiApp.models import *

from PIL import Image 
import cv2

try:
   pisettings_instance = PiSettings.objects.get(id =1)
except:
   pisettings_instance = PiSettings.objects.create(id =1)

html_source_header = "application/webcam/django/html/"
static_source_header = "static/webcam/django/static/"
camera = None

def index(request):
    t = get_template(html_source_header + 'webcam.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def image(request):
    global camera
    http = HttpResponse(mimetype='image/jpeg')
    if camera != None:
        retval, im = camera.read()      
        img = Image.open('/home/ubuntu/PiBox/App/webcam/django/static/img/pi_logo.png')
        img.save(http,'png')
        # img = Image.frombytes("RGB", (size_x, size_y), im)
        # img.save(http,'jpg')
    return http

def open_camera(request):
    global camera
    try:
        if request.method == 'GET':  
            camera_port = int(request.GET['camera_port']) 
            camera = cv2.VideoCapture(camera_port)
            return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))   

def close_camera(request):
    global camera
    # del(camera)
    return HttpResponse(simplejson.dumps({'msg':'ok'}))   