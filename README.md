# PiBox #
PiBox is an interesting Smart Home demo.<br>
http://wzyy2.github.io/PiBox

# 介绍 #
写这个PiBox的初衷是现在智能硬件的概念很火,打着家庭网关称号的路由器层出不穷,什么智能家居拉,带摄像头拉,控制家电拉,做小车阿,作者也手痒,于是就着手开始做这么一个web base的嵌入式交互应用(好文绉绉..).

# 功能 #
内置了yaaw和系统信息显示,(yyaw需要配合aria2,所以输入sudo apt-get install aria2)<br>
默认自带的app只有gpio(由于手上的树梅派不见了,所以还未完成,建议也加参数删除).<br>
更多的app可以在optional-app里选.<br>

# Usage #

首先安装全部的依赖环境.

    sudo apt-get install python-pip python-dev build-essential  libjsoncpp-dev python-pil
    sudo apt-get install python-setuptools
    sudo pip install Django==1.6.6
    sudo apt-get install scons

下面执行安装脚本(在PiBox文件夹下).

    sudo sh ./install_source.sh (如果不是树梅派的话，请加-g 0,将不会安装gpio控制)
    sudo sh ./install_env.sh
如果有问题，可以自己打开脚本一条一条输，看返回信息

    sudo sh ./start.sh 
    sudo sh ./stop.sh
这是程序的启停脚本,注意sudo sh ./start.sh哦.
最后进浏览器,输入

    http://192.168.10.105(换成你的ip):8000
(注意文件管理器的默认目录是/home/shares）

# Technical details #
PiBox由两部分组成,分别是c++程序和django的web界面,两者之间通过socket通信,之所以这样做也是为了确保功能的灵活性,c++能实现更多的功能.<br>
如果要扩展应用,可以参考examples-app的写一个程序放到APP文件夹,见example-app的readme.

## License ##
PiBox is free software;you can redistribute it and/or modify it under terms of the GNU General Public License version 2 as published by the Free Software Foundation.

## PS ##
如果你有什么问题的话,欢迎通过qq和email联系我~地址在我个人主页可以找到~（好希望自己的代码能有人玩嘛 T T）
提供人肉支持~

## FAQ ##
* [FAQ](https://github.com/wzyy2/PiBox/wiki)



## Image ##
![image](http://www.iotwrt.com/jpg/pibox1.jpg)
![image](http://www.iotwrt.com/jpg/pibox2.jpg)
![image](http://www.iotwrt.com/jpg/pibox3.jpg)
![image](http://www.iotwrt.com/jpg/pibox4.png)
