from django.db import models


#It's better to name model with prefix app's name
#sh/syncdb.py  should be run after eidt models
class sns_test(models.Model):
    new_field = models.CharField(max_length=100)



