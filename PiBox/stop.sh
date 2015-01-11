#!/bin/sh

# killall pihome
# killall python

PID=$(cat /var/run/pihome.pid) 
kill -9 $PID
pids=`ps aux|grep 'manage.py'|grep -v 'grep'|awk -F' ' '{print $2}'`
if [ "$pids" ];then
   kill -9 $pids
fi