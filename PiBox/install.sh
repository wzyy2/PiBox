#!/bin/sh
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}
cp -rf ./etc/* /etc
mkdir /home/shares
chmod 0777 /home/shares