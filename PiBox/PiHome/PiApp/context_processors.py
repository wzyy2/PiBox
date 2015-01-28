#coding=utf-8
'''
# The modules contains global template data

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from common import globaldata
from common.api import notification

# notification.send('i', 0, 'title', 'test!')

def app_info(request):
    return  {
        'PCILIST': globaldata.pci_list.content,
        'NOTIFICATION': notification.get_unread(request.user.id),
    }

def version(request):
    return  {
        'VERSION': globaldata.VERSION,
    }