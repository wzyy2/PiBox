#!/bin/bash

option=$1
install_dir=$2

if [[ $option != "-f" ]]; then
    #statements
    echo "please add parameter -f"
    exit
fi

dir=`dirname ${0}`
dir2="${PWD}/${dir}"
cd ${dir2}

cp -rf ./* $install_dir