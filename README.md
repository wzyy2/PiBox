# PiBox #
PiBox is an interesting Smart Home demo.<br>
http://wzyy2.github.io/PiBox

# Usage #
See these steps for a  build guide(cd Pibox).<br>
First install the dependencies:

    sudo apt-get install python-pip python-dev build-essential  libjsoncpp-dev python-pil
    sudo apt-get install python-setuptools
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

## License ##
PiBox is free software;you can redistribute it and/or modify it under terms of the GNU General Public License version 2 as published by the Free Software Foundation.

# 介绍 #
写这个PiBox的初衷是现在智能硬件的概念很火,打着家庭网关称号的路由器层出不穷,什么智能家居拉,带摄像头拉,控制家电拉,做小车阿,作者也手痒,于是就着手开始做这么一个web base的嵌入式交互应用(好文绉绉..).

# 功能 #
内置的功能有yaaw和系统信息显示(yyaw需要配合aria2,所以输入sudo apt-get install aria2),除此之外还有一些专门的app应用<br>
可以在optional-app里选,目前有gpio控制和摄像头截图.<br>

# Details #
PiBox由两部分组成,分别是c++程序和django的web界面,两者之间通过socket通信,之所以这样做也是为了确保功能的灵活性,c++能实现更多的功能.<br>
如果要扩展应用,可以参考examples-app的写一个程序放到APP文件夹,见example-app的readme.

## PS ##
如果你有什么问题的话,欢迎通过qq和email联系我~地址在我个人主页可以找到~（好希望自己的代码能有人玩嘛 T T）
提供人肉支持.

## FAQ ##
* [FAQ](https://github.com/wzyy2/PiBox/wiki)



## Image ##
![image](http://www.iotwrt.com/jpg/pibox1.jpg)
![image](http://www.iotwrt.com/jpg/pibox2.jpg)
![image](http://www.iotwrt.com/jpg/pibox3.jpg)
![image](http://www.iotwrt.com/jpg/pibox4.png)
