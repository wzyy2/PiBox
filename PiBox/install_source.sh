#!/bin/bash
dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}

#cd ./lib/jsoncpp-src-0.5.0
#scons platform=linux-gcc
#cp libs/linux-gcc-4.6/libjson_linux-gcc-4.6_libmt.a /usr/local/lib/libjsonlib.a
#cd ../
#cd ../

if_gpio=1

while getopts g: option
do 
    case "$option" in
        g)
            if_gpio=$OPTARG
        # \?)
        #     echo "Usage: args [-h n] [-m] [-s]"
        #     echo "-h means hours"
        #     echo "-m means minutes"
        #     echo "-s means seconds"
        #     exit 1;;
    esac
done


cd CppClient
scons
if [ $? -ne 0 ];then
    echo "error!"
    exit
fi
cd ../



# if [ "$if_gpio" = 1 ]; then
#     cd lib/WiringPi-master
#     chmod 0777 ./build
#     ./build
#     if [ $? -ne 0 ];then
#         echo "error!"
#         exit
#     fi
#     cd ../
#     cd ../
#     cd App/GPIO
#     scons
#     if [ $? -ne 0 ];then
#         echo "error!"
#         exit
#     fi
#     cd ../
#     cd ../
# else
#     rm -rf App/GPIO    
# fi

