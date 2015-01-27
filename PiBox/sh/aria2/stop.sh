#!/bin/sh

pids=`ps aux|grep 'aria2'|grep -v 'grep'|awk -F' ' '{print $2}'`
if [ "$pids" ];then
   kill -9 $pids
fi

echo 'kill aria2!'