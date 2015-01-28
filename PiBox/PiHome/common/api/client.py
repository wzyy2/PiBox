#coding=utf-8
'''
# deprecated!
# communication with CPP client.

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

import re,os
import sys
from socket import *
import json as simplejson

#client
class PiRturn():
    connect = False
    message = {}

def  socketjson_send(serverHost, serverPort,send_message):
    pi_ret = PiRturn()
    try:
        #建立一个tcp/ip套接字对象
        sockobj = socket(AF_INET, SOCK_STREAM)
        #连结至服务器及端口
        sockobj.settimeout(5)
        sockobj.connect((serverHost, serverPort))
        #经过套按字发送line至服务端
        sockobj.send(simplejson.dumps(send_message))
        #从服务端接收到的数据，上限为1k
        #data = sockobj.recv(1024)
        #关闭套接字
        sockobj.close( )
        pi_ret.connect = True
#        pi_ret.message = simplejson.dumps({'msg':'fail'}) 
    except:
        pi_ret.connect = False
#        pi_ret.message = simplejson.dumps({'msg':'fail'}) 

    return pi_ret

def  socketjson_send_recv(serverHost, serverPort,send_message):
    pi_ret = PiRturn()
    try:
        #建立一个tcp/ip套接字对象
        sockobj = socket(AF_INET, SOCK_STREAM)
        #连结至服务器及端口
        sockobj.settimeout(5)
        sockobj.connect((serverHost, serverPort))
        #经过套按字发送line至服务端
        sockobj.send(simplejson.dumps(send_message))
        #从服务端接收到的数据，上限为1k
        data = sockobj.recv(2048)
        #关闭套接字
        sockobj.close( )
        pi_ret.connect = True
        pi_ret.message = simplejson.loads(data) 
    except:
        pi_ret.connect = False

    return pi_ret

def  socket_test(serverHost, serverPort):
    pi_ret = PiRturn()
    try:
        #建立一个tcp/ip套接字对象
        sockobj = socket(AF_INET, SOCK_STREAM)
        #连结至服务器及端口
        sockobj.settimeout(2)
        sockobj.connect((serverHost, serverPort))
        #经过套按字发送line至服务端
        sockobj.send("hello")
        #从服务端接收到的数据，上限为1k
        #data = sockobj.recv(1024)
        #关闭套接字
        sockobj.close( )
        pi_ret.connect = True
#        pi_ret.message = simplejson.dumps({'msg':'fail'}) 
    except:
        pi_ret.connect = False
#        pi_ret.message = simplejson.dumps({'msg':'fail'}) 

    return pi_ret.connect

