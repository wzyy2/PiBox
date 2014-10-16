#!/bin/sh


if [ ! -f "/etc/PiBox/aria2/save/aria2.session" ]; then
    touch '/etc/PiBox/aria2/save/aria2.session'
fi

#if [ ! -f "/var/PiBox/aria2/save/aria2.log" ]; then
#    touch '/var/PiBox/aria2/save/aria2.log'
#fi

aria2c --conf-path="/etc/PiBox/aria2/aria2c.conf" -D
