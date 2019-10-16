#!usr/bin/python
#-*-coding:utf-8-*-
#a=[12,34,54,65,76,87]
#for i,j in enumerate(a):
 #   print(i,j)
#a=int(input('输入你选中数据'))
#import random
#a=random.randrange(10)
#for i in range(3):
#    num=int(input('请输入一个数字'))
 #   if 10>=num > a:
 #       print('猜大了，还剩{}次').format(2-i)
#import random
#a=random.randrange(6)
#for i in range(3)
 #   b=input('请输入大/小')
#    if b=='大':
  #      if 0<a<=3
#i=0
#hile i<3:
##    a=0
 #   while a<3:
 #      a+=1
  #    print('hao')
#for i in range (1,10):
#    for j in range (1,i+1):
#        print('{}*{}={}'.format(j,i,i*j),end=' ')
#    print()
#i=6
#while i>0:
 #   j=0
  #  while j<i-1:
#        print('*',end=' ')
#        j+=1
#    print()
#    i-=1#a=int(input('输入a:'))
#b=int(input('输入b:'))
#sum=0
#for i in range(a,b+1):
  #  k=2
  # if i >=2:
  #      while i % k !=0:

   #         k +=1
   #     if i==k:
  #          sum += i
#print(sum)
#for i in  range(100,1000):
#   a=i//100
#   b=i//10%10
#   c=i%10
 #  if a**3+b**3+c**3==i:
 #       print(i)











#for i in range(1,10):
  #  for j in range(1,i+1):
 #       print('{}*{}={}'.format(i,j,i*j),end=' ')
 #   print()
#j=0
#b=0
#while j<5:
 #   j=j+1
#    b=b+j
#p##rint(b)
#for i in range(100,1000):
 #  a=i//100
 ###      print(i)
 #a='ab'
 #b='ni'
 #print(a)
 #print(b)
 #c=''
 #c=a
 #def hanshu():
  #   a=0
  #   for i in range(10,12):
  #       a=a+i
  #       print(a)
#c=han
#a=[25,24,35,0,12,34,12]
#for i in range(len(a)):
#    for j in range(i+1,len(a)):
#        if a[i]>a[j]:
#            a[i],a[j]=a[j],a[i]
#    print(a)
# try:
#     print('sjasda')
#     raise TypeError('出错了')
# except TypeError:
#     print(123)
#
# else:
#     print()
#





# import xlwt   #导入xlwt模块
# xl=xlwt.Workbook(encoding='utf-8') #设置excel文件的格式
# sheet=xl.add_sheet('python_test')#sheet name
# for i in range(1,10):   #向标签页里写入内容，第一个代表行  第二个代表列  第三个写入的是内容
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# xl.save('a.xls')

# import xlwt
# ss=xlwt.Workbook(encoding='ansi')
# sheet


#
# import xlrd
# xr =xlrd.open_workbook('a.xls')
# b=xr.nsheets
# print(b)
# sheet=xr.sheets()[0]
# '''
# '''
# name=xr.sheet_names()
# print(name)
# sheet=xr.sheet_by_name('python_test')
# hanshu=sheet.nrows
# print(hanshu)
# hang3=sheet.row_values(2)
# print(hang3)
# lieshu=sheet.ncols
# print(lieshu)
# lie3=sheet.col_values(2)
# print(lie3)
# gezi=sheet.cell(0,0).value
# print(gezi)
# from xlutils.copy import copy
# import xlrd
# yuan_file=xlrd.open_workbook('a.xls')
# new_file=copy(yuan_file)#复制文件，并不是直接写入到原文件里，
#而是复制一份新文件在操作，只有写入功能，没有读取功能
# sheet=new_file.get_sheet(0)#获取要操作的标签页，get_sheet(下标位置）
# a=open('qqq.txt','r',encoding='ansi')
# b=a.readlines()
# c=0
# for i in b:
#     sheet.write(c,0,i)
#     c+=1
# new_file.save('a.xls')

# print(sheet)
# sheet.write(0,0,1111)
# new_file.save('a.xls')


# import time
# a=time.time()
# print(a)
# b=time.localtime()
# print(b)
# c=time.gmtime()
# print(c)#将结构化时间转换为格式化时间
# print(time.strftime('%Y-%m-%d %X',time.localtime()))#将结构化时间转换为格式化时间  #%X时分秒==%H:%M:%S时分秒
#print(time.strptime('2019/09/18 10:05:28','%Y/%m/%d %X'))#格式化时间转换为结构化时间
# import time
# from time import sleep
# start=time.time()
# for i in range(3):
#     sleep(3)
#     print(i)
# end=time.time()
# print(end-start)
# a =[i for i in range(10)]+[chr(i)for i in range(97,103)]
# b = int(input('>>>'))
# f =[]
# while True:
#     d=b%16
#     b=b//16
#     f.append(a[d])
#     if b==0:
#         break
# f.reverse()
# print(f)
# import xlwt
# # xl = xlwt.Workbook(encoding='utf-8')
# # sheet=xl.add_sheet('python_test')
# # sheet.write(1,0,'xieru')
# # xl.save('a.xls')
# import xlrd
# xr = xlrd.open_workbook('b.xls')
# a=xr.nsheets
# name=xr.sheet_names()
# sheet=xr.sheet_by_name('nei')
# hangshu=sheet.nrows
# lieshu=sheet.ncols
# with open('qqq.txt','w',encoding='utf-8')as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang=sheet.cell(i,j).value
#             x.write(hang +' ')
# import xlwt
# xr=xlwt.Workbook(encoding='utf-8')
# sheet=xr.add_sheet('nei')
# with open('a.txt','r',encoding='utf-8')as a:
#     b=a.readlines()
#     for i,j in enumerate(b):
#         k=j.split(',')
#         for m,n in enumerate(k):
#             sheet.write(i,m,n)
# xr.save('b.xls')
# import pymysql
# class Mysql_learn(object):
#     def __init__(self):
#         #链接数据库
#         self.conn = pymysql.connect(host='192.168.2.128',port=3306,user='root',passwd='123456',db='test')
#         #设置游标
#         self.su=self.conn.cursor()
#
#     def cao_zuo(self):
#         # 执行sql语句 execute 获取sql语句的结果的个数
#         self.su.execute('show databases;')
#         # self.su.execute('show tables;')
#         # 读取上一个sql语句执行的结果
#         #fetchall 读取所有内容
#         #fetchone 读取一条内容
#         #self.su.execute('delete from biao;')
#         # ferchmany 读取多条内容，默认是一条 例如（4）读取4条内容
#         #         #fetchall数据，只有在对某个表的数据进行添加（insert），删除（delete），更改（alter）
#         self.conn.commit
#         #断开链接
#         self.conn.close()
#         print(self.su.fetchone())
#
# d = Mysql_learn()
# d.cao_zuo()
import os





#popen()执行cmd命令
# dd=os.popen('notepad')
# print(dd.read())

#getcwd  获取当前所在的目录
# print(os.getcwd())


#chdir 切换目录
# os.chdir('C:')
# print(os.getcwd())

#mkdir 创捷目录
# os.mkdir('aaa')

#创建递归目录
# os.makedirs('eee/qqq/www')

#删除递归目录
# os.removedirs('eee/qqq/www')

#删除空目录
# os.rmdir('aaa')

#删除文件
# os.remove('qqq.txt')

#文件重命名
# os.rename('day10.py','买鸡.py')

#获取目录下的所有文件 listdir
# print(os.listdir('C:'))

#将文件名与路径分隔开
# aa=os.path.split(r'‪F:\pycharm\pycharm\kang\新建文本文档.txt')
# print(aa)
#将文件后缀名与路径分隔开
# aa= os.path.splitext(r'‪F:\pycharm\pycharm\kang\新建文本文档.txt')
# print(aa)
#判断文件是否是目录：是  显示 true 不是 false
# aa = os.path.isdir(r'report')
# print(aa)


#



# a=print(os.listdir('F:'))
# for i in range(len(a)):
#     b=os.path.isdir(r'a[i]')
#     if b == True:
#         c.append(b)
#     else:
#         d.append(b)

# 统计当前目录下有多少目录文件，
# 有多少个普通文件
# 1.当前目录所有文件获取到
# 2.循环判断这个文件是普通文件还是目录文件


# a,b=0,0
# for i in os.listdir():
#     if os.path.isdir(i):
#         a+=1
#     else:
#         b+=1
# print(b)
#将当前目录下的所有的.py过滤到列表



# 列表推导式
# a= [i for i in os.listdir() if os.path.splitext(i)[1]=='.py']
# print(a)

# 输入一个日期例如 ：
import time
a=time.localtime()
print(a)


