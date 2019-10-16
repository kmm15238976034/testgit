#!/usr/bin/python
#-*-coding:utf8-*-




#paramiko  封装了ssh协议，主要用于远程控制
import paramiko
#创建一个ssh客户端
ssh123 = paramiko.SSHClient()
# 将第一次连接的主机跳过验证
# 并添加到know_host文件中
ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh123.connect(hostname='192.168.2.143',port=22,username='root',password='123456')
stuin,stuout,stuerr =ssh123.exec_command('ls -ll')
#stuin ：指的是输入的命令
#stuout：命令运行后的结果
#stuerr:命令的报错
aa = stuout.read().decode('utf-8')
print(aa)
#断开连接
ssh123.close()

