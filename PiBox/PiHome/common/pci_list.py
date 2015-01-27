#coding=utf-8
'''
# This modules contains pihome control interface list, which used to create sidebar for pihome.

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.core.urlresolvers import reverse
import os,sys

'''
    pihome control interface list,will be used to create sidebar and titlebar 
'''
class PciList():
    def __init__(self):
        self.content = list()

    def register(self, title, url, font):
        a = dict()
        a['title'] = title
        a['url'] = url
        a['font'] = font
        a['child'] = list()
        self.content.append(a)

    def addchild(self, title, url, parent):
        for item in self.content:
            if item['title'] ==  parent:
                a = dict()
                a['title'] = title
                a['url'] = url
                item['child'].append(a)
                break 

    def applist(self):
        for item in self.content:
            if item['title'] ==  'application':
                return item['child'] 

    def urldict(self):
        a = dict()
        for item in self.content: 
            a[item['title']] = item['url']
        return a

    def delete(self):
        pass

