#!/usr/bin/python
#-*-coding:utf8-*-
# class Sweetpotato:
#     #定义属性，一般用来完成一些初始化的工作
#    def __init__(self):
#       self.cookedlevel=0
#       self.cookedString='生的'
#       self.condiments=[]
#    def __str__(self):
#        msg='地瓜的生熟程度：'+self.cookedString
#        msg+='\n地瓜的等级为：'+str(self.cookedlevel)
#        msg+='\n添加佐料为：'
#        if len(self.condiments)>0:
#            for i in self.condiments:
#                msg+=i+','
#            msg=msg.rstrip(',')
#        else:
#            msg+='当前没有添加佐料'
#        return msg
#    def cook(self,times):
#        self.cookedlevel+=times
#        if self.cookedlevel>8:
#            self.cookedString='烤成木炭'
#        elif self.cookedlevel>5:
#            self.cookedString='已经烤好了'
#        elif self.cookedlevel>3:
#            self.cookedString='半生不熟'
#        else:
#            self.cookedString='生的'
#    def addconfiments(self,temp):
#        self.condiments.append(temp)
# digua=Sweetpotato()
# print(digua)
# digua.cook(2)
# digua.addconfiments('芥末')
# print(digua)
# digua.cook(3)
# digua.addconfiments('番茄')
# print(digua)



#将txt写入excel
# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('nei')
# with open('a.txt','r',encoding='utf-8')as  a:
#     b=a.readlines()
#     for i,j in enumerate(b):
#         k = j.split(',')
#         for m,n in enumerate(k):
#             sheet.write(i,m,n)
# xr.save('b.xls')
#将excel写入txt
# import xlrd
# xr = xlrd.open_workbook('b.xls')
# a = xr.nsheets
# name = xr.sheet_names()
# sheet = xr.sheet_by_name('nei')
# hangshu = sheet.nrows
# lieshu = sheet.ncols
# with open('999.txt','w',encoding='utf-8') as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang = sheet.cell(i,j).value
#             x.write(hang+' ')
# import xlwt
# xl = xlwt.Workbook(encoding='utf-8')
# sheet = xl.add_sheet('sheet1')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%s*%s=%s'%(j,i,j*i))
# xl.save('wqww.xls')
# print('over')
# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet2')
# for i in range(1,10):
#     for j in range (1,i+1):
#         sheet.write(i-1,j-1,'%s*%s=%s'%(j,i,j*i))
# xr.save('aaaa.xls')

# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet1')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%s*%s=%s'%(j,i,j*i))
# xr.save('aaaa.xls')


# import xlrd
# xr=xlrd.open_workbook('b.xls')
# a=xr.nsheets
# name=xr.sheet_names()
# sheet=xr.sheet_by_name('nei')
# hangshu=sheet.nrows
# lieshu=sheet.ncols
# with open('a.txt','w',encoding='utf-8')as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang=sheet.cell(i,j).value
#             x.write(hang+' ')
# import xlwt
# xr=xlwt.Workbook(enconding='utf-8')
# sheet=xr.add_sheet('sheet1')
# with open('a.txt','r',encoding='utf-8')as a:
#     b=a.readlines()
#     for i,j in enumerate(b):
#         k=j.split(',')
#         for m,n in enumerate(k):
#             sheet.write(i,m,n)
# xr.save('b.xls')
# import xlrd
# xr=xlrd.open_workbook('b.xls')
# a=xr.nsheets
# name=xr.sheet_names()
# sheet=xr.sheet_by_name('nei')
# hangshu=sheet.nrows
# lieshu=sheet.ncols
# with open('qqq.txt','w',encoding='utf-8')as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang=sheet.cell(i,j).value
#             x.write(hang+' ')


# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet2')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%d*%d=%d'%(j,i,j*i))
# xr.save('ccc.xls')





# import xlrd
# xr=xlrd.open_workbook('ccc.xls')
# #a=xr.nsheets
# name=xr.sheet_names()
# sheet=xr.sheet_by_name('sheet2')
# hangshu=sheet.nrows
# lieshu=sheet.ncols
# with open('a.txt','w',encoding='utf-8')as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang =sheet.cell(i,j).value
#             x.write(hang +'  ')

# import xlwt
# with open('a.txt','w',encoding='utf-8')as a:
#     a.write('a,b,c,d\n,e,f,g\n')
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet1')
# with open('a.txt','r',encoding='utf-8')as a:
#     b=a.readlines()
#     for i,j in enumerate(b):
#         k=j.split(',')
#         for m,n in enumerate(k):
#             sheet.write(i,m,n)
# xr.save('b.xls')
# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet = xr.add_sheet('sheet1')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%s*%s=%s'%(j,i,j*i))
# xr.save('ccc.xls')
# import pymysql
# class Mysql_learn(object):
#     def__init__(self):
#     self

# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet1')
# with open ('a.txt','r',encoding='utf-8')as x:
#     y=x.readlines()
#     for i,j in enumerate(y):
#         # print(j)
#         # print(type(j))
#         z=j.split(',')
#         for m,n in enumerate(z):
#             #print(n)
#             sheet.write(i,m,n)
# xr.save('b.xls')
# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('sheet1')
# with open('a.txt','r',encoding='utf-8')as x:
#     y=x.readlines()
#     for i,j in enumerate(y):
#         z=j.split(',')
#         for m,n in enumerate(z):
#             sheet.write(i,m,n)
# xr.save('b.xls')
# import pymysql
# class Mysql_learn(object):
#     def __init__(self):
#         self.conn=pymysql.connect(host='192.168.2.118',__import__())
import smtplib
import email.mime.text
import email.mime.multipart
sender='kmm15238976034@163.com'
reser='1713336089@qq.com','285402577@qq.com'
server='smtp.163.com'
passwd='kmm123'
message=email.mime.multipart.MIMEMultipart()
message['From']=sender
message['To']='',join(reser)
message['subject']='python_learn'
aa="""一条长河天上来
"""