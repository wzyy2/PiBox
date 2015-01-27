#/bin/env python
# -*-coding:utf8-*-
'''
# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
import urllib  
import json

if __name__ == '__main__':

    choose = int(raw_input('1.write   2.read   3.edit   4.remove   5.history'))
    domain = raw_input('domain(as 192.168.10.106:8000) : ')
    sensor_id = raw_input('sensor_id(int) : ')

    #write
    if choose == 1:
        a = list()
        ex = 'y'
        while ex == 'y':
            key = raw_input('key(as 2012-12-12T11:11:11) : ')
            value = float(raw_input('value(float) : '))   
            a.append({'value': value, 'key' : key})
            ex = raw_input('again?y or n    ')

        #raw post
        params = json.dumps(a)
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/", params)
        #get
        # params = urllib.urlencode({'value': value, 'key' : key})
        # f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/?%s" % params)
        get = f.read()
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
        key = raw_input('key(as 2012-12-12T11:11:11) : ')
        value = float(raw_input('value(float) : '))     
        params = urllib.urlencode({'key': key, 'value' : value})
        f = urllib.urlopen("http://" + domain + "/API/sensor/" + sensor_id + "/datapoint/edit/?%s" % params)
        get = f.read()
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