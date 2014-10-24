#!/bin/sh
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}

cd ./lib/jsoncpp-src-0.5.0
scons platform=linux-gcc
cp libs/linux-gcc-4.6/libjson_linux-gcc-4.6_libmt.a /usr/local/lib/libjsonlib.a
cd ../
cd ../
cd CppClient
scons
cd ../

cd App/Camera
scons
cd ../
cd ../

cd App/GPIO
scons
cd ../
cd ../

cd App/Location
scons
cd ../
cd ../

cd lib/django-filebrowser-no-grappelli-master
python setup.py install
cd ../
cd WiringPi-master
chmod 0777 ./build
./build