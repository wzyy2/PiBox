import os,re

GPIO_DIR = '/sys/class/gpio'

class gpio(object):
    def __init__(self, num):
        self.NUM = num

    def gpio_export(self):
        os.system('echo' + ' ' + str(self.NUM) + ' ' + '>' + ' ' + GPIO_DIR + '/export')

    def write_gpio_direction(self, direction):
        os.system('echo' + ' ' + direction + ' ' + '>' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/direction')

    def write_gpio_value(self, value):
        os.system('echo' + ' ' + str(value) + ' ' + '>' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/value')

    def gpio_unexport(self):
        os.system('echo' + ' ' + str(self.NUM) + ' ' + '>' + ' ' + GPIO_DIR + '/unexport')           

    def read_gpio_direction(self):
        direction = os.popen('cat' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/direction').read()  
        return direction

    def read_gpio_value(self):
        value = os.popen('cat' + ' ' + GPIO_DIR + '/gpio' + str(self.NUM) + '/value').read()  
        return int(value)

def gpio_exists(num):
    return os.path.exists(GPIO_DIR + '/gpio' + str(num))

def scan_gpio():
    gpio_list = os.listdir(GPIO_DIR)
    ret = list()
    for item in gpio_list:
        if os.path.isdir(os.path.join(GPIO_DIR, item)):
            match = re.match('gpio\d*$', item)
            if match: 
                ret.append(match.group(0))
    return ret
            
