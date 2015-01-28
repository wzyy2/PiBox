#coding=utf-8
'''
# This modules is used to handle gpio with sysfs interface

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

import os,re

GPIO_DIR = '/sys/class/gpio'

class gpio(object):
    def __init__(self, num):
        self.NUM = num

    def gpio_export(self):
        os.system('echo' + ' ' + str(self.NUM) + ' ' + '>' + ' ' + GPIO_DIR + '/export')

    ## @brief change the direction of gpio
    # @param    string    "in","out"
    def write_gpio_direction(self, direction):
        os.system('echo' + ' ' + direction + ' ' + '>' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/direction')

    def write_gpio_value(self, value):
        os.system('echo' + ' ' + str(value) + ' ' + '>' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/value')

    def gpio_unexport(self):
        os.system('echo' + ' ' + str(self.NUM) + ' ' + '>' + ' ' + GPIO_DIR + '/unexport')           

    ## @brief get the direction of gpio
    # @return string   "in","out"
    def read_gpio_direction(self):
        direction = os.popen('cat' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/direction').read()  
        return direction

    def read_gpio_value(self):
        value = os.popen('cat' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/value').read()  
        return int(value)

## @brief identify if gpio exists  
# @param    int    the num of gpio
# @return bool
def gpio_exists(num):
    return os.path.exists(GPIO_DIR + '/gpio' + str(num))

## @brief scan for exported gpio
# @return list  as "gpio1","gpio2" 
def scan_gpio():
    gpio_list = os.listdir(GPIO_DIR)
    ret = list()
    for item in gpio_list:
        if os.path.isdir(os.path.join(GPIO_DIR, item)):
            match = re.match('gpio\d*$', item)
            if match: 
                ret.append(match.group(0))
    return ret
            
