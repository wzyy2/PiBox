'''
# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
import os,sys

cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
sys.path.append(os.path.join(cwd, 'PiHome'))

print 'Sensor:', str(sys.argv[1])
print 'Value:', str(sys.argv[2])
print 'key:', str(sys.argv[3])