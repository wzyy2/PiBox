import os,sys

cwd = os.path.dirname(os.path.abspath(__file__)) + '/..'
pihome_dir = cwd + '/PiHome'
app_dir = cwd + '/App'
sync_dir = pihome_dir + '/web_source'

list = os.listdir(app_dir)

for item in list:
    item_dir = os.path.join(app_dir, item)
    if os.path.isdir(item_dir):
        models = os.path.join(item_dir, 'web_source/models.py')
        if os.path.exists(models):
            os.system('cp ' + models + ' ' + sync_dir)
            os.system("python " + pihome_dir + '/manage.py' + " syncdb")
            os.system('rm -f' + ' ' + sync_dir + '/models.py' )



