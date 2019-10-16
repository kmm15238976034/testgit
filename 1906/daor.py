#!/usr/bin/python
#-*-coding:utf8-*-
#使用paramiko模块中的sftpclient组件传输文件
#1.建立一个传输通道，填入ip地址和端口号（是一个元组）
# import paramiko
# # transport=paramiko.Transport(('192.168.2.143',22))
# # #2.连接主机，只需要输入用户名和密码
# # transport.connect(username='root',password='123456')
# # #3.创建一个sftp的客户端
# # sftp_client=paramiko.SFTPClient.from_transport(transport)
# # #4.从linux传文件到windows get('远程主机上文件的路径’，‘本地主机上的路径’）
# # sftp_client.get('a.txt',r'F:\pycharm\pycharm\b.txt')
# # #5.从windows上传文件到linux
# # sftp_client.put(r'F:\pycharm\pycharm\b.txt'')





#爬小说
import requests
import re
class Chong_sheng(object):
    def __init__(self,url,bianma,lv):
        self.url = url
        self.bianma = bianma
        self.lv = lv
    def qing_qiu(self):
        head = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
               }
        req = requests.get(self.url,headers=head)
        bian = req.content.decode(self.bianma)
        return bian
    def guo_lv(self):
        guo = re.compile(self.lv,re.S)
        zhengwen = guo.findall(self.qing_qiu())
        print(zhengwen)
        for i in zhengwen:
            m = i.replace('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;','\n')
            n = m.replace('<br /><br />','')
            print(n)
            return n
    def bao_cun(self):
        with open('重生.txt','a',encoding='utf-8') as f:
            f.write(self.guo_lv())

cc = Chong_sheng('https://www.65ws.com/a/8/8752/2654616.html','gbk','&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(.*?)www.65ws.com。')
cc.qing_qiu()
cc.guo_lv()
cc.bao_cun()
