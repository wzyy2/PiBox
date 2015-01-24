上传数据
============================
注意，所有的时间(key,start,end)用标准时间格式，例如：2012-03-15T16:13:14 或者
2012-03-15 16:13:14。
开关传感器
--------------------------------------------------
| url   | 作用   |  方法  |  请求参数 | 返回参数  |
| -------- | -----:  | :----:  | :----:  |:----:  |
| /API/home/datapoint/|修改|GET|sensor_id，value| json = {'msg'} |
| /API/home/datapoint/get/|查询|GET|sensor_id|json = {'msg', 'value}|

数值传感器
--------------------------------------------------
| url   | 作用   |  方法  |  请求参数 | 返回参数  |
| -------- | -----:  | :----:  | :----:  |:----:  |
| /API/home/datapoint/|新增|GET，POST|GET（sensor_id，key，value）or POST（body : {'key','value'} or [{'key','value'}]）+ GET（sensor_id) | json = {'msg'} |
| /API/home/datapoint/get/|查询|GET|sensor_id，key|json = {'msg', 'value}|
| /API/home/datapoint/edit/|修改|GET|sensor_id，key，value| json = {'msg'} |
| /API/home/datapoint/remove/|删除|GET|sensor_id，key| json = {'msg'} |
| /API/home/datapoint/history/|历史（时间段）|GET|sensor_id,start,end,interval(间隔，单位秒）| json = {'msg'， 'datapoint'=[{'value','key'}] |
| /API/home/datapoint/history/|历史（返回最新前二十条）|GET|sensor_id| json = {'msg'， 'datapoint'=[{'value','key'}]} |
json data could be like this：

    {
      "key":"2012-03-15T16:13:14",
      "value":294.34
    }
or

    [
      {"key": "2012-06-15T14:00:00", "value":315.01},
      {"key": "2012-06-15T14:00:10", "value":316.23},
      {"key": "2012-06-15T14:00:20", "value":317.26},
      {"key": "2012-06-15T14:00:30", "value":318},
      {"key": "2012-06-15T14:00:40", "value":317}
    ]
图像传感器
--------------------------------------------------
懒的写了。。。自己看PiApp.api.py里的从new_datapoint_json起往下,和数值差不多，不过不支持批量，get的value全换成post上传文件。。。

Example
--------------------------------------------------
暂无
CallBack
============================
Explain
--------------------------------------------------
Callback file是传感器满足条件后被调用的python代码文件名（比如callback_file=gpio.py)，同时文件需要放在PiBox/sh/callback/下。
不使用的话只需提供不存在的文件名或者保持为空即可。

对开关传感器来说，每一次开关数值点发生修改，callback_file都会被按如下格式调用

        python callback_file sensor.name swtich_status(1 or 0)
        
对数值传感器来说,每一次新增或者修改的数值都会检查条件，如果满足条件，callback_file都会被按如下格式调用

        python callback_file sensor.name value（溢出的数值） key（时间）
        
Example
--------------------------------------------------
在sh/callback下有两个文件实例可以直接使用
### gpio.py

    import os,sys
    
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
    sys.path.append(os.path.join(cwd, 'PiHome'))
    
    from common import linux_gpio
    
    print 'Sensor:', str(sys.argv[1])
    print 'Status:', str(sys.argv[2])
    
    GPIO_NUM = 23
    
    print 'GPIO_BCM_NUM:', GPIO_NUM
    
    gpio = linux_gpio.gpio(GPIO_NUM)
    gpio.gpio_export()
    gpio.write_gpio_direction('out')
    gpio.write_gpio_value(sys.argv[2])
在需要的开关传感器下填入gpio.py,将文件的GPIO_NUM改成所需的gpio编号，每次开关状态改变，就会带动gpio改变。
### callout.py

    import os,sys

    print 'Sensor:', str(sys.argv[1])
    print 'Value:', str(sys.argv[2])
    print 'key:', str(sys.argv[3])
在需要的数值传感器下填入callout.py和条件,数值发生改变时条件若满足，会发送debug信息到log里。