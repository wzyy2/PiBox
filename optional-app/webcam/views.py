#coding=utf-8
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required 
import json as simplejson 

from PIL import Image 
import cv2,os
import cv2.cv as cv

from common import globaldata

cwd  = globaldata.BASE_DIR + '/App/webcam/'

camera = None

@login_required  
def index(request, title='webcam', belong=['application']):
    t = get_template('webcam/webcam.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def image(request):
    global camera
    http = HttpResponse(mimetype='image/jpeg')
    if camera != None:
        #skip cache
        for i in range(5):
            retval, img = camera.read()      
        cv2.imwrite(cwd + "tmp/tmp.jpg" , img)
        ret_img = Image.open(cwd + "tmp/tmp.jpg")
        ret_img.save(http,'JPEG')
    else:
        ret_img = Image.open(cwd + "tmp/cancel.png")
        ret_img.save(http,'png')       
    return http

def open_camera(request):
    global camera
    try:
        camera_port = int(request.GET['camera_port']) 
        if camera == None:
            camera = cv2.VideoCapture(camera_port)
            camera.set(cv.CV_CAP_PROP_FRAME_WIDTH,320)
            camera.set(cv.CV_CAP_PROP_FRAME_HEIGHT,240)
            camera.set(cv.CV_CAP_PROP_FPS,12)
            retval, img = camera.read()      #light led
        return HttpResponse(simplejson.dumps({'msg':'ok'}))   
    except: 
        return HttpResponse(simplejson.dumps({'msg':'fail'}))   

def close_camera(request):
    global camera
    camera.release()
    camera = None
    return HttpResponse(simplejson.dumps({'msg':'ok'}))   


# CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
# CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
# CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# CV_CAP_PROP_FPS Frame rate.
# CV_CAP_PROP_FOURCC 4-character code of codec.
# CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# CV_CAP_PROP_HUE Hue of the image (only for cameras).
# CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# CV_CAP_PROP_WHITE_BALANCE Currently unsupported
# CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)