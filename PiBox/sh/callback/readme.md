上传数据
============================

**值类型**：

- msg：'ok'  or  'fail'
- key：datetime, such as 2012-03-15T16:13:14  or 
2012-03-15 16:13:14。
- value： url(as '/pibox_upload/xxxx')  or  float


开关传感器
--------------------------------------------------
| url   | 作用   |  方法  |  请求参数 | 返回参数  |
| -------- | -----:  | :----:  | :----:  |:----:  |
| /API/sensor/{sensor_id}/datapoint/|修改|GET|value`int`| {'msg'} |
| /API/sensor/{sensor_id}/datapoint/get/|查询|GET||{'msg', 'value'}|

数值传感器
--------------------------------------------------
| url   | 作用   |  方法  |  请求参数 | 返回参数  |
| ------- | :-----:  | :----:  | :------:  |  :----:  |
| /API/sensor/{sensor_id}/datapoint/|新增|GET | key`datetime`，value`float`|  {'msg'} |
| /API/sensor/{sensor_id}/datapoint/|新增|POST| [{'key' : `datetime`, 'value' : `float`}] |  {'msg'} |
| /API/sensor/{sensor_id}/datapoint/get/|查询|GET|key`datetime`| {'msg', 'value'}|
| /API/sensor/{sensor_id}/datapoint/edit/|修改|GET|key`datetime`，value`float`| {'msg'} |
| /API/sensor/{sensor_id}/datapoint/remove/|删除|GET|key`datetime`|  {'msg'} |
| /API/sensor/{sensor_id}/datapoint/history/|历史（时间段）|GET|start`datetime`, end`datetime`, interval`int(seconds）`| {'msg'， 'datapoint'=[{'value','key'}] |
| /API/sensor/{sensor_id}/datapoint/history/|历史（返回最新前二十条）|GET|  | {'msg'， 'datapoint'=[{'value','key'}]} |
json data could be like this：
```
    {
      "key":"2012-03-15T16:13:14",
      "value":294.34
    }
```
or
```
    [
      {"key": "2012-06-15T14:00:00", "value":315.01},
      {"key": "2012-06-15T14:00:10", "value":316.23},
      {"key": "2012-06-15T14:00:20", "value":317.26},
      {"key": "2012-06-15T14:00:30", "value":318},
      {"key": "2012-06-15T14:00:40", "value":317}
    ]
```

图像传感器
--------------------------------------------------
| url   | 作用   |  方法  |  请求参数 | 返回参数  |
| ------- | :-----:  | :----:  | :------:  |  :----:  |
| /API/sensor/{sensor_id}/datapoint/|新增|POST | key`datetime`，value`file`|  {'msg'} |
| /API/sensor/{sensor_id}/datapoint/get/|查询|GET|key`datetime`| {'msg', 'value`url`'}|
| /API/sensor/{sensor_id}/datapoint/edit/|修改|GET|key`datetime`，value`file`| {'msg'} |
| /API/sensor/{sensor_id}/datapoint/remove/|删除|GET|key`datetime`|  {'msg'} |
| /API/sensor/{sensor_id}/datapoint/history/|历史（时间段）|GET|start`datetime`, end`datetime`, interval`int(seconds）`| {'msg'， 'datapoint'=[{'value`url`','key'}] |
| /API/sensor/{sensor_id}/datapoint/history/|历史（返回最新前二十条）|GET|  | {'msg'， 'datapoint'=[{'value`url`','key'}]} |
ret can be like this
```
    {
      "key":"2012-03-15T16:13:14",
      "value":"/media/pibox_upload/pic_datapoint/111.png"
    }
```
注意返回的都是url，具体图片再从url读

Example
--------------------------------------------------
在sh/datapoint_tools下有使用urllib的数据测试脚本，可以用来增删数据，也可以用来做例子。
[开关传感的读写脚本](https://github.com/wzyy2/PiBox/tree/master/PiBox/sh/datapoint_tools/switch.py)
[数据传感的CURD脚本](https://github.com/wzyy2/PiBox/tree/master/PiBox/sh/datapoint_tools/num.py)
[图片传感的CURD脚本](https://github.com/wzyy2/PiBox/tree/master/PiBox/sh/datapoint_tools/pic.py)
使用办法如下
```
输入python switch.py
输出1.write   2.read 选择 1
输出domain(as 192.168.10.106:8000) : 输入192.168.10.106:8000
输出sensor_id(int) : 输入 1
输出value(int) : 输入 1
```
只要对这些脚本稍加修改，另外加上一些python代码就可以通过以下思路，实现自己的本地智能家居：
* 通过串口等通讯模块，关联单片机，然后关联上native yeelink。
* 通过驱动读取树莓派所接模块的数据，然后上传数据到native yeelink。

CallBack
============================
Callback file是传感器满足条件后被调用的python代码文件名`比如gpio.py`，被调用的文件需要放在PiBox/sh/callback/下(重启有效)。
不使用的话只需提供不存在的文件名或者保持为空即可。

对开关传感器来说，每一次开关数值点发生修改，callback_file都会被按如下格式调用

        python callback_file sensor.name swtich_status(1 or 0)
        
对数值传感器来说,每一次新增或者修改的数值都会检查条件，如果满足条件，callback_file都会被按如下格式调用

        python callback_file sensor.name value（溢出的数值） key（时间）
     
        
Case
--------------------------------------------------
在sh/callback下有几个文件实例可以直接使用
### gpio.py（开关）

    import os,sys
    
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
    sys.path.append(os.path.join(cwd, 'PiHome'))
    
    from common.driver import linux_gpio
    
    print 'Sensor:', str(sys.argv[1])
    print 'Value:', str(sys.argv[2])
    
    GPIO_NUM = 23
    
    print 'GPIO_BCM_NUM:', GPIO_NUM
    
    gpio = linux_gpio.gpio(GPIO_NUM)
    gpio.gpio_export()
    gpio.write_gpio_direction('out')
    gpio.write_gpio_value(sys.argv[2])
在需要的开关传感器下填入gpio.py,将文件的GPIO_NUM改成所需的gpio编号，每次开关状态改变，就会带动gpio改变。
直接使用这个脚本就可以通过web来控制简单电器

### callout.py（数值）

    import os,sys

    print 'Sensor:', str(sys.argv[1])
    print 'Value:', str(sys.argv[2])
    print 'key:', str(sys.argv[3])
在需要的数值传感器下填入callout.py和条件,数值发生改变时条件若满足，会发送debug信息到log里。

### send_email.py（数值）
发邮件到指定邮箱，需要修改账号密码，详见sh/callback

others
============================
Any issues or improvements please contact jacob-chen@iotwrt.com