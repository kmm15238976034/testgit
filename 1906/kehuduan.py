#!/usr/bin/python
#-*-coding:utf8-*-
#客户端
#客户端不需要绑定IP和监听
import socket
while True:
    sock=socket.socket()
    #客户端虽然不需要绑定ip  但是连接服务器
    sock.connect(('192.168.2.117',66))
    #发送请求
    #输入请求的内容
    message=input('请输入内容：')
    #发送请求的内容给服务器
    sock.send(message.encode('utf-8'))
    #接收服务器的响应
    recive=sock.recv(1024)
    print(recive.decode('utf-8'))
    #断开数据库
    sock.close()