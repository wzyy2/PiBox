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

./CppClient/pihome &  
python ./PiHome/WebShell/webshell.py --ssl-disable 0 & 
python ./PiHome/manage.py runserver 0.0.0.0:8000 & 