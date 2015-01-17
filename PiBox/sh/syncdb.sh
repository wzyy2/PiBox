#!/bin/sh
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}
cd ../

python ./PiHome/manage.py syncdb

