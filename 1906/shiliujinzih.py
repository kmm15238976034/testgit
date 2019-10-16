#!/usr/bin/python
#-*-coding:utf8-*-
#a=open('123.txt','r')
#print(a.read())
#class lei():
#    pass
#lei()
#class Cat:
    #属性：
    #方法
#    def eat(self):
#  #       print('---吃----')
#  ##   def drink(self):
# #        print('---喝---')
#  #   def lashi(self):
# #         print('---拉---')
# #     def sleep(self):
# #         print('---睡---')
# # big_flower_cat=Cat()
# # big_flower_cat.eat()
# # big_flower_cat.drink()
# # big_flower_cat.lashi()
# # big_flower_cat.sleep()
# #ying_duan=Cat()
# #ying_duan.eat()
# #big_flower_cat.color='花色'
# #print(big_flower_cat.color)
# #big_flower_cat.weba='有'
# #print(big_flower_cat.weba)
# #big_flower_cat.leg = '四条'
# #print(big_flower_cat.leg)
# #big_flower_cat.prinfo()
# #dabaimao=Cat()
# #dabaimao.color='白'
# #dabaimao.weiba='有'
# #dabaimao.prinfo()
# class Cat():
#     def __init__(self,newweiba,newcolor):
#         self.weiba=newweiba
#         self.color=newcolor
#
#     def __str__(self):
#         msg = '有没有尾巴:' + self.weiba +'\n颜色:'+self.color
#         return msg
# #        print('--吃--')
#  #   def dirnk(self):
#  #       print('--喝--')
#
# xiaohuamao = Cat('有','花色')
# # print(xiaohuamao)
#
# class Student:
#     def __init__(self):
#         self.name='空的'
#     def hanshu(self):
#         print(120)
#     def hanshu1(self):
#         print(110)
# class KdStudent(Student):
#     pass
# lapwang=KdStudent()
#
# class Animal():
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print('say hello')
# class Pig(Animal):
#     def talk(self):
#         print('hengheng')
# class Dog(Animal):
#         print('wangwang')
# class Student:
#     def hanshu(self):
#         print('niha')
# class KdStudent(Student):
#     pass
# laowang=KdStudent()
# laowang.hanshu()
# class Home:
#     def __init__(self,newarea):
#         self.area=newarea
#         self.containsitems=[]
#     def __str__(self):
#         msg='家当前可用面积为：'+str(self.area)+'平方米'
#         msg+='\n家里目前的家具有：'
#         if len(self.containsitems)>0:
#             for i in self.containsitems:
#                 msg+=i.name+','
#             msg=msg.strip(',')
#         else:
#             msg+='当前没有家具'
#         return msg
#     def additems(self,item):
#         if self.area>item.area:
#             self.containsitems.append(item)
#             self.area-=item.area
# class Bed:
#     def __init__(self,newname,newarea):
#         self.name=newname
#         self.area=newarea
#     def __str__(self):
#         msg='床的面积为：'+str(self.area)+'平方米'
#         msg+='\n床的样式为：'+self.name
#         return msg
# home=Home(110)
# print(home)
# bed=Bed('席梦思',4)
# print(bed)
# home.additems(bed)
# print(home)
# import xlrd
# xr=xlrd.open_workbook('b.xls')
# name=xr.sheet_names()
# sheet=xr.sheet_


















import smtplib #封装smtp协议
import email.mime.text  #处理正文中的数据
import email.mime.multipart #邮件的格式
sender = 'kmm15238976034@163.com'
reser='1713336089@qq.com','285402577@qq.com '
server='smtp.163.com'
#授权码
passwd='kmm123'
message=email.mime.multipart.MIMEMultipart()
#添加发件人，收件人，主题
message['From']=sender
message['TO']=''.join(reser)
message['Subject']='python_learn'
aa="""哎意义一样
"""
cc = email.mime.text.MIMEText(aa)
att1 = email.mime.text.MIMEText(open(r'dongtai.py', 'rb').read(), 'base64', 'utf-8')
# 附件携带的字段和值
att1["Content-Type"] = 'application/octet-stream'
# 附件携带的字段和值  这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
# 将附件添加到邮件里
message.attach(att1)
att2 = email.mime.text.MIMEText(open(r'a.txt', 'rb').read(), 'base64', 'utf-8')
# 附件携带的字段和值
att2["Content-Type"] = 'application/octet-stream'
# 附件携带的字段和值  这里的filename可以任意写，写什么名字，邮件中显示什么名字
att2["Content-Disposition"] = 'attachment; filename="abc.txt"'
message.attach(att2)


#将正文添加到邮件里
message.attach(cc)
#定义发送邮件的服务器和端口号
smtp123=smtplib.SMTP_SSL(server,465)
#登陆服务器
smtp123.login(sender,passwd)
smtp123.sendmail(sender,reser,message.as_string())
smtp123.close()
message.attach(cc)

#定义发送的附件的文件名，文件可以是任何格式的
# att2=email.mime.text.MIMEText(open('dongtai.py','rb').read(),'base64','utf-8')
# #附件携带的字段和值
# att2["Content-Type"]='application/octet-stream'
# #附件携带的字段和值 这里的filename 可以任意
# att2["Content-Disposition"]='attachment;filename="test.txt"'
# #将附件添加到邮件里
# message.attach(att2)