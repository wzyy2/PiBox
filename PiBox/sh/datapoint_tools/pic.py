#/bin/env python
# -*-coding:utf8-*-
'''
# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
import urllib
import urllib2  
import sys
import json

try:
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
except:
    print "In order to post file,you should install poster modules!!"
    print "sudo pip install poster"

if __name__ == '__main__':

    choose = int(raw_input('1.write   2.read   3.edit   4.remove   5.history'))
    domain = raw_input('domain(as 192.168.10.106:8000) : ')
    sensor_id = raw_input('sensor_id(int) : ')

    #write
    if choose == 1:
        filepath = raw_input('filepath(as ./xxx.jpg) : ')
        key = raw_input('key(as 2012-12-12T11:11:11) : ')

        # 在 urllib2 上注册 http 流处理句柄
        register_openers()

        # 开始对文件的 multiart/form-data 编码
        # "value" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置
        # headers 包含必须的 Content-Type 和 Content-Length
        # datagen 是一个生成器对象，返回编码过后的参数，这里如果有多个参数的话依次添加即可
        datagen, headers = multipart_encode({"value": open(filepath, "rb"), "key" : key})

        request = urllib2.Request("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/", datagen, headers)

        get = urllib2.urlopen(request).read()
        print 'ret body:', get
        s = json.loads(get)
        print 'msg:', s['msg']

    #read
    elif choose == 2:
        key = raw_input('key(as 2012-12-12T11:11:11) : ')
        params = urllib.urlencode({'key': key})
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/get/?%s" % params)
        get = f.read()
        print 'ret body:', get
        s = json.loads(get)
        print 'key:',s['key'],'value:',s['value']

    #edit
    elif choose == 3:
        filepath = raw_input('filepath(as ./xxx.jpg) : ')
        key = raw_input('key(as 2012-12-12T11:11:11) : ')

        # 在 urllib2 上注册 http 流处理句柄
        register_openers()

        # 开始对文件的 multiart/form-data 编码
        # "value" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置
        # headers 包含必须的 Content-Type 和 Content-Length
        # datagen 是一个生成器对象，返回编码过后的参数，这里如果有多个参数的话依次添加即可
        datagen, headers = multipart_encode({"value": open(filepath, "rb"), "key" : key})

        request = urllib2.Request("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/edit/", datagen, headers)

        get = urllib2.urlopen(request).read()
        print 'ret body:', get
        s = json.loads(get)
        print 'msg:', s['msg']

    #remove
    elif choose == 4:
        key = raw_input('key(as 2012-12-12T11:11:11) : ')
        params = urllib.urlencode({'key': key})
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/remove/?%s" % params)
        get = f.read()
        print 'ret body:', get
        s = json.loads(get)
        print 'msg:', s['msg']

    #history
    elif choose == 5:
        ex = raw_input('latest 20?y or n')
        if ex == 'y':
            f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/history/")
            get = f.read()
            print 'ret body:', get
            s = json.loads(get)
            for item in s['datapoint']:
                print 'key:',item['key'],'value:',item['value']
        else:
            start = raw_input('start(as 2012-12-12T11:11:11) : ')
            end = raw_input('end(as 2012-12-12T11:11:11) : ') 
            interval = raw_input('interval(int) : ')   
            params = urllib.urlencode({'start': start, 'end' : end, 'interval' : interval})         
            f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/history/?%s" % params)
            get = f.read()
            print 'ret body:', get
            s = json.loads(get)
            for item in s['datapoint']:
                print 'key:',item['key'],'value:',item['value']            