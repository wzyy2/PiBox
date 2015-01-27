#coding=utf-8
'''
# The modules contains global template data

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from common import globaldata


def app_info(request):
    return  {
        'PCILIST': globaldata.pci_list.content,
    }

def version(request):
    return  {
        'VERSION': globaldata.VERSION,
    }