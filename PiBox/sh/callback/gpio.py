'''
# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
import os,sys


cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
sys.path.append(os.path.join(cwd, 'PiHome'))

from common.driver import linux_gpio

print 'Sensor:', str(sys.argv[1])
print 'Value:', str(sys.argv[2])

GPIO_NUM = 23

print 'GPIO_BCM_NUM:', GPIO_NUM

gpio = linux_gpio.gpio(GPIO_NUM)
gpio.gpio_export()
gpio.write_gpio_direction('out')
gpio.write_gpio_value(sys.argv[2])