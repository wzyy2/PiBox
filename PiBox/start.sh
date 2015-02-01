#!/bin/sh
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}

echo '+---+   +    + +---+ +-+-+ +--+'
echo '|   |   |    | |   | | | | |   '
echo '|   | + |    | |   | | | | +--+'
echo '+---+   +----+ |   | | | | |   '
echo '|     + |    | |   | | | | |   '
echo '|     | +    + +---+ + + + +--+'
echo '|     |                        '
echo '+     +             Hello World'

ret=`netstat -an |grep 8000`
if [ "$ret" ];then
   echo 'A program is already using port 8000 '
   exit
fi
ret=`netstat -an |grep 8001`
if [ "$ret" ];then
   echo 'A program is already using port 8001'
   exit
fi
ret=`netstat -an |grep 3333`
if [ "$ret" ];then
   echo 'A program is already using port 3333'
   exit
fi

echo "Attention : If you can't see anything in the browser, please check log in log/pihome.log"

ip=`ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'`

echo "http://$ip:8000  or others"

nohup ./CppClient/pihome > ./log/cpp.log 2>&1 &  
nohup python ./PiHome/WebShell/webshell.py --ssl-disable 0 > ./log/pihome-webshell.log 2>&1 & 
nohup python ./PiHome/manage.py runserver 0.0.0.0:8000 > ./log/pihome.log 2>&1 & 