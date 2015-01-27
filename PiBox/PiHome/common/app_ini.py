'''
# This modules is used to read conf from registered app.

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

import ConfigParser
import string, os, sys


class AppIni():
    def __init__(self, get_dir):
        self.base_dir = get_dir
    
    def read(self, app, arg1):
        app_dir = os.path.join(self.base_dir, app)
        cf = ConfigParser.ConfigParser()
        cf.read(os.path.join(app_dir, "app.ini"))  

        return cf.get('Application', arg1)

