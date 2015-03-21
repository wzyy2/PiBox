# PiBox #
PiBox is a web control Interface running on Embedded Board, written in python and django.<br>
With PiBox，you can do things like that:
![image](http://www.iotwrt.com/jpg/pb1.png)
## Usage 
See these steps for a  build guide(cd Pibox).<br>
First install the dependencies:

    sudo apt-get install python-pip python-dev build-essential  libjsoncpp-dev libjpeg-dev zlib1g-dev
    sudo apt-get install python-setuptools
    sudo pip install pillow
    sudo pip install Django==1.6.6
    sudo apt-get install scons

Then run building script:

    sudo sh ./install_source.sh
    sudo sh ./install_env.sh
Start and stop scripts:

    sudo sh ./start.sh 
    sudo sh ./stop.sh

After run the start script,open your browser and go to the URL:

    http://192.168.10.105(your board's ip):8000
(File browser use /home/shares）

uninstall and reinstall：
    delete the folder and do these steps again.

## Feature
* native iot platform(connect your hardwares to web, like yeelink).
* File Browser.
* Web ssh.
* host status monitor.
* webcam snapshot.
* GPIO control.
* [more here](https://github.com/wzyy2/PiBox/wiki/Feature)

## License 
PiBox is free software;you can redistribute it and/or modify it under terms of the GNU General Public License version 2 as published by the Free Software Foundation.

## PS
If you want more background on how it works,create an issue or email me:-).

## FAQ 
* [FAQ](https://github.com/wzyy2/PiBox/wiki/FAQ)



## Image 
![image](http://www.iotwrt.com/jpg/pb2.jpg)
![image](http://www.iotwrt.com/jpg/pb3.jpg)

# Chinese #
## 介绍 
写这个PiBox的初衷是现在智能硬件的概念很火,打着家庭网关称号的路由器层出不穷,什么智能家居拉,带摄像头拉,控制家电拉,做小车阿,作者也手痒,于是就着手开始做这么一个web base的嵌入式交互应用(好文绉绉..).
## App 
如果要扩展应用,可以参考optional-app的写一个程序放到APP文件夹.
如果要使用已有的app，请参考optional-app的readme.