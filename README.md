# PiBox #
PiBox is an interesting Smart Home demo.


#妈蛋英语太烂，下面先写中文,以后再说#
# 介绍 #
写这个PiBox的初衷是现在智能硬件的概念很火，作者是学习嵌入式的学生，就想搞一些来玩玩。
偶然间接触到了树莓派，因为之前搞过一个openwrt的控制，就很想在树莓派上做一个类似小米路由器+boardlink这样一个东西。因为网上一些网页控制例子简直太弱了，就想搞个高大上一点的东西。

# 功能 #
没功能。。。嗯，现在就只是一个可以参考的框架而已，由于我没开发应用。唯一有用的就是内置了yaaw和文件管理器和系统信息显示，可以当个nas界面和监视界面。
## Usage ##  
    sudo apt-get install python-pip python-dev build-essential 
    sudo pip install Django==1.6.6
    sudo pip install PIL 
    apt-get install python-setuptools
这是安装django用的，先确保你安装了pip和python哈。

    apt-get install scons
这个是项目的构建工具~
然后执行安装脚本

    sudo sh ./install_lib.sh
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
如果要扩展应用，可以参考examples-app的写一个c++程序放到APP文件夹，python的代码放到PiHome\PiApp\application这里。
# 后续 #
现在还只是个简单的框架，首先我没有写文档，可能很多地方代码会看不懂，其次我也没有在上面做应用做示范，现在屁功能都没有，工程也没做改动，等以后有空吧。
在截图里你可能看到了安卓客户端，这个也是我写的，不过还不是很完善，如果对智能硬件产品的Android客户端有兴趣的人很多的话，我再完善然后放出吧。

还有使用说明很不完善，纯粹瞎写~~~。。。如果有疑问，提供人肉支持~。

# 问题 #
最大的问题还是django的debug模式暴露了太多东西出来，用软连接组织app和django的联系也有很多麻烦呐，如果暴露出来安全性堪忧。。。。

## License ##
PiBox is free software;you can redistribute it and/or modify it under terms of the GNU General Public License version 2 as published by the Free Software Foundation.
当然，你们有商业化用途的准备的话或者准备用做自己的产品的话我也很高兴~不过希望能发邮件让我知道你们使用了这个方案或者里面的代码\(˙<>˙)/然后我换个许可证就可以啦~.

## PS ##
如果你有什么问题的话，或者不爽我写的代码，或者有什么样的需求想我加上，或者想一起写~欢迎通过qq和email联系我~地址在我个人主页可以找到~（好希望自己的代码能有人玩嘛 T T）
提供人肉支持~



![image](http://www.iotwrt.com/jpg/pibox1.jpg)
![image](http://www.iotwrt.com/jpg/pibox2.jpg)
![image](http://www.iotwrt.com/jpg/pibox3.jpg)
![image](http://www.iotwrt.com/jpg/pibox4.png)
