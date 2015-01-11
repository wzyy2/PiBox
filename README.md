# PiBox #
PiBox is an interesting Smart Home demo.<br>
http://wzyy2.github.io/PiBox

# 介绍 #
写这个PiBox的初衷是现在智能硬件的概念很火，作者是学习嵌入式的学生，就想搞一些来玩玩。
偶然间接触到了树莓派，因为之前搞过一个openwrt的控制，就很想在树莓派上做一个类似小米路由器+boardlink这样一个东西。因为网上一些网页控制例子简直太弱了，就想搞个高大上一点的东西。

# 功能 #
没功能。。。嗯，现在就只是一个可以参考的框架而已，由于我没开发应用。唯一有用的就是内置了yaaw和文件管理器和系统信息显示，可以当个nas界面和监视界面。
（yyaw需要配合aria2，所以输入sudo apt-get install aria2,配合chrome上的百度网盘助手导出到树莓派使用更佳~）<br>
默认自带的参考app只有gpio（还不能用，也只能在树莓派编译，其他平台需要加参数删除），更多的app可以在optional-app里选。

# Usage #
    sudo apt-get install python-pip python-dev build-essential  libjsoncpp-dev
    sudo apt-get install python-setuptools
    sudo pip install Django==1.6.6
    sudo pip install PIL 
这是安装django用的，先确保你安装了pip和python哈。

    sudo apt-get install scons
这个是项目的构建工具~
然后执行安装脚本

    sudo sh ./install_lib.sh （如果不是树梅派的话，请加-g 0,将不会安装gpio控制)
    sudo sh ./install.sh
如果有问题，可以自己打开脚本一条一条输，看返回信息

    sudo sh ./start.sh 
    sudo sh ./stop.sh
来运行开启，关闭程序了。
进浏览器，输入

    http://192.168.10.105(换成你的ip):8000
就OK啦~（大概。。。不行我人肉支持。。。）
(注意文件管理器的默认目录是/home/shares）



# Technical details #
他由两部分组成，分别是一个c++程序和django的web界面，两者之间通过socket通信，之所以这样做也是为了确保功能的灵活性，c++能实现更多的功能。（= =其实python换lua更好呢，不管啦）
如果要扩展应用，可以参考examples-app的写一个程序放到APP文件夹,见example-app的readme.
# 后续 #
现在还只是个简单的框架，屁功能都没有，等以后有空。
在截图里你可能看到了安卓客户端，这个也是我写的，不过还不是很完善，如果对Android客户端有兴趣的人很多的话，我再完善然后放出。

如果有疑问，提供人肉支持~。

# 问题 #
最大的问题觉得是安全性堪忧。。。。

## License ##
PiBox is free software;you can redistribute it and/or modify it under terms of the GNU General Public License version 2 as published by the Free Software Foundation.
## PS ##
如果你有什么问题的话，或者不爽我写的代码，或者有什么样的需求想我加上，或者想一起写~欢迎通过qq和email联系我~地址在我个人主页可以找到~（好希望自己的代码能有人玩嘛 T T）
提供人肉支持~



![image](http://www.iotwrt.com/jpg/pibox1.jpg)
![image](http://www.iotwrt.com/jpg/pibox2.jpg)
![image](http://www.iotwrt.com/jpg/pibox3.jpg)
![image](http://www.iotwrt.com/jpg/pibox4.png)
