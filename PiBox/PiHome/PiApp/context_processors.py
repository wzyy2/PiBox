#coding=utf-8
from common import globaldata


def app_info(request):
    return  {
        'PCILIST': globaldata.pci_list.content,
    }

def version(request):
    return  {
        'VERSION': globaldata.VERSION,
    }