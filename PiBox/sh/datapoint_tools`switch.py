#/bin/env python
# -*-coding:utf8-*-
'''
# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
import urllib  
import json

if __name__ == '__main__':

    choose = int(raw_input('1.write   2.read '))
    domain = raw_input('domain(as 192.168.10.106:8000) : ')
    sensor_id = raw_input('sensor_id(int) : ')

    if choose == 1:
        value = int(raw_input('value(int) : '))        
        # params = urllib.urlencode()
        params = urllib.urlencode({'value': value})
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/?%s" % params)
        get = f.read()
        print 'ret body:', get

        s = json.loads(get)
        print 'msg:', s['msg']

    elif choose == 2:
        # params = urllib.urlencode()
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/get/")
        get = f.read()
        print 'ret body:', get

        s = json.loads(get)
        print 'value:', s['value']
