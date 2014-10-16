# PiBox #
PiBox is an interesting Smart Home demo.


#妈蛋英语太烂，下面先写中文,以后再说#
# 介绍 #
写这个PiBox的初衷是现在智能硬件的概念很火，作者是学习嵌入式的学生，就想搞一些来玩玩。
偶然间接触到了树莓派，因为之前搞过一个openwrt的控制，就很想在树莓派上做一个类似小米路由器+boardlink这样一个东西。因为网上一些网页控制例子简直太弱了，就想搞个高大上一点的东西。

# 功能 #
没功能。。。嗯，现在就只是一个可以参考的框架而已，由于我没开发应用。唯一有用的就是内置了yaaw和文件管理器和系统信息显示，可以当个nas界面和监视界面。
## Usage ##
    pip install Django==1.6.6
    sudo apt-get install python-pip python-dev build-essential 
这是安装django用的，先确保你安装了pip和python哈。

    mkdir /home/shares
这个是建立shares文件夹，django内置的文件管理器目录和minidlna，smaba，aria2默认下载目录都用这个。
然后就是安装一个ftp，samba或者minidlana目录设置为/home/shares了，其实我不建议用minidlna啦，难用的要死，直接ftp，samba就够看电影了。怎么安装这几个。。。你们谷歌吧。。
解压github上下到的文件到你的目录~
然后就是编译c++程序，在编译之前看看你有没有jsoncpp，没有的话

    cd lib\jsoncpp-src-0.5.0
然后谷歌linux jsoncpp看看如何安装。。。。

    apt-get install scons
这个是项目的构建工具~
然后进CppClient文件夹。

    scons
来编译cpp程序。

    sudo sh ./install.sh
 这个是把要用到配置文件安装起来（目前只有aria2的配置文件）。   
    
    cd lib\django-filebrowser-no-grappelli-master
    sudo python setup.py install
这个是安装文件管理器。
然后大概就可以

    sudo sh ./start.sh 
    sudo sh ./stop.sh
来运行开启，关闭程序了。
进浏览器，输入

    http://192.168.10.105(换成你的ip):8000
就OK啦~（大概。。。不行我人肉支持。。。）



# Technical details #
他由两部分组成，分别是一个c++程序和django的web界面，两者之间通过socket通信，之所以这样做也是为了确保功能的灵活性，c++能实现更多的功能。（= =其实python换lua更好呢，不管啦）
如果要扩展应用，可以参考examples-app的写一个c++程序放到APP文件夹，python的代码放到PiHome\PiApp\application这里。
# 后续#
现在还只是个简单的框架，首先我没有写文档，可能很多地方代码会看不懂，其次我也没有在上面做应用做示范，现在屁功能都没有，工程也没做改动，等以后有空吧。
在截图里你可能看到了安卓客户端，这个也是我写的，不过还不是很完善，如果对智能硬件产品的Android客户端有兴趣的人很多的话，我再完善然后放出吧。

还有使用说明很不完善，纯粹瞎写~~~。。。如果有疑问，提供人肉支持~。

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
