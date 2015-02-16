#!/bin/sh
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}
cp -rf ./etc/* /etc
# ln -s ${dir2}/App  PiHome/templates/application
# ln -s ${dir2}/App  PiHome/static/application
ln -s ${dir2}/App  PiHome

mkdir /home/shares
chmod 0666 /home/shares