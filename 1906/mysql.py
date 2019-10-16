#!/usr/bin/python
#-*-coding:utf8-*-
import pymysql#用来连接与操作数据库的
conn = pymysql.connect(host='192.168.2.128',port=3306,user='root',passwd='123456',db='pachong',charset='utf-8')
#cusor=conn.cursor()                                                               #连接数据库，charset是数据库统一编码
#cusor.execute('create database pachong;'#创建数据库
#cusor.execute('show databases;')#查看数据库
#conn.commit()#提交数据
#conn.close#断开连接

#创建游标
cusor=conn.cursor()
#cusor.execute('create table biaoming(name char);')
print(cusor.execute('show tables;'))
conn.commit()
conn.close()
print(cusor.fetchmany())#默认只显示一个结果的第一个值
print(cusor.fetchall())#获取上一句sql语句执行结果