#coding=utf-8
'''
# This modules contains piapp’s notification api

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''
from django.db.models import Q
from PiApp.models import Notification


## @brief send Notification
# @param    string    the type of Notification, 'd''i''w'
# @param    int    the id of user, 0 for all
# @param    text    title
# @param    text    the text to send
# @return Notification
def send(type, user_id, title, content):
   return Notification.objects.create(type = type, user_id = user_id, title = title, content = content)

## @brief get unread Notification 
# @param    int    the id of user
# @return personal Notification, all-user Notification
def get_unread(user_id):
    ret1 = Notification.objects.filter(Q(user_id = user_id, has_readed = False) | Q(user_id = 0, has_readed = False))
    return ret1

## @brief get unread Notification and set has_readed to true
# @param    int    the id of user
# @return personal Notification, all-user Notification
def get_unread_clear(user_id):
    ret1 = Notification.objects.filter(Q(user_id = user_id, has_readed = False) | Q(user_id = 0, has_readed = False))
    for item in ret1:
        item.has_readed = True
        item.save()
    return ret1

## @brief get all Notification 
# @param    int    the id of user
# @return personal Notification, all-user Notification
def get_all(user_id):
    ret1 = Notification.objects.filter(Q(user_id = user_id) | Q(user_id = 0))
    return ret1

## @brief delete   Notification
# @param    int   the id of Notification
def delete(not_id):
    return Notification.objects.get(id = not_id).delete()
