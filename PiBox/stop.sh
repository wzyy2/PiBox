#!/bin/sh

# killall pihome
# killall python

pids=`ps aux|grep 'pihome'|grep -v 'grep'|awk -F' ' '{print $2}'`
if [ "$pids" ];then
   kill -9 $pids
fi
pids=`ps aux|grep 'manage.py'|grep -v 'grep'|awk -F' ' '{print $2}'`
if [ "$pids" ];then
   kill -9 $pids
fi
pids=`ps aux|grep 'webshell.py'|grep -v 'grep'|awk -F' ' '{print $2}'`
if [ "$pids" ];then
   kill -9 $pids
fi