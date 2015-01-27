#coding=utf-8
'''
# send email to the specified mailbox when num callback had been called

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

import os,sys
import socket
import fcntl
import time
import struct
import smtplib
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#发送邮件的基本函数，参数依次如下
# smtp服务器地址、邮箱用户名，邮箱秘密，发件人地址，收件人地址（列表的方式），邮件主题，邮件html内容
def sendEmail(smtpserver,username,password,sender,receiver,subject,msghtml):
    msgRoot = MIMEMultipart('related')
    msgRoot["To"] = ','.join(receiver)
    msgRoot["From"] = sender
    msgRoot['Subject'] =  subject
    msgText = MIMEText(msghtml,'html','utf-8')
    msgRoot.attach(msgText)
    #sendEmail
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()



if __name__ == '__main__':
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/..' + '/..'
    sys.path.append(os.path.join(cwd, 'PiHome'))

    # 传感器名字
    sensor = str(sys.argv[1])
    # 溢出值
    value = str(sys.argv[2])
    # 时间
    key =  str(sys.argv[3])

    content = "Sensor Name : " + sensor + "\n"
    content += "Value : " + value + "\n"
    content += "Time : " + key + "\n"

    sendEmail('smtp.163.com','account','passwd','sender addr',['receiver addr'],'PiBox',content)
    # sendEmail('服务器','网易邮箱账号','网易邮箱密码','发件人地址',['收件人地址'],'title',content)