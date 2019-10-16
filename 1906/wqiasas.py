#!/usr/bin/python
#-*-coding:utf8-*-
# a=[12,34,45,56,]
# for i in  range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
#             #break
# # print(a)
# a=int(input('>>>'))
# if a%2==0 and a%3==0:
#     print('hello world')
#     if a%2==0:
#         print('hello')
#         if a%3==0:
#             print('world')
# else:
#     print(123)
# a=input()
# b=str(a)
# fiag=True
# for i in range(len(b)/2):
#     if b[i] != b[len(b) - i - 1]:
#         flag = False
#         break
# a=[1,2,3,3,4,]
# # for i in  range(len(a)):
# #      for j in range(i+1,len(a)):
# #          if a[i]>a[j]:
# #              a[i],a[j]=a[j],a[i]
# a.sort()
# a.reverse()
# print(a)





# l=[2,3,3,4]
# print(l)
# i=0
# max1=l[0]
# max2=l[0]
# while i<len(l):
#     if max1 < l[i]:
#         max2 = max1
#         max1 = l[i]
#     else:
#         if max2 < l[i]:
#                 max2 = l[i]
#     i = i + 1
# print("max1:",max1)
# print("max2:",max2)

#
# a = int(input('>>>'))
# while a> 5:
#     print('hello')
# a=4
# while a>5:
#     print(123)
# else:
#     print(234)
# a=0
# sum=0
# while a <=100:
#     sum=sum+a
#     a+=1
# print(sum)
#
# def qwe(*args,**kwargs):
#     print(args)
#     print(kwargs)
# qwe( 2,12,a='23',b='qqq')
# def qwe(x):
#     b=0
#     for i in range(x+1):
#         b+=i
#     print(b)
# qwe(10)




# a='5678'
# b=a[::-1]
# c=0
# d=0
# for i in range(len(b)):
#     for j in range(10):
#         if str(j)==b[i]:
#             c=j*10**i
#             d+=c
# print(d)
# print(type(d))
# #
#
#
#
# a=[1,2,3,4]
# a.append(a[0])
# a.pop(0)
# print(a)
# b=[1,2,3,4]
# b.append(3)
# b.sort()
# print(b)
# a=[1,2,3,4]
# a.append(5)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             a[i],a[j]=a[i],a[j]
# # print(a)
# a='7676'
# b=a[::-1]
# c=0
# d=0
# for i in range(len(b)):
#     for j in range(10):
#         if str(j)==b[i]:
#             c=j*10**i
#             d+=c
# print(d)


# a=[1234]
# print(type(a))
# a=input('一个国家')
# if a.startswith('我')and a.endswith('你'):
#     print('hao')
# else:
#     print('nihao')
# import pymysql
# class Mysql_learn(object):
#     def __init__(self):
#         self.conn = pymysql.connect(host='192.168.2.128', port=3306, user='root', passwd='123456', db='test')
#         self.su = self.conn.cursor()
#     def cao_zuo(self):
#         self.su.execute('show tables;')
#         #self.su.execute('show tables;')
#         print(self.su.fetchall())
#     #    self.su.execute('create table nine(da char(20),xiao char(20));')
#     #    self.su.execute('insert into nine values("i","j");')
#     #     for x in range(101):
#     #         self.su.execute('insert into nine values("aaa","bbb");')
#     #         self.conn.commit()
#         #self.su.execute('select * from nine;')
#      #   self.su.execute('delete from nine where da="i";')
#         # c = self.su.fetchall()
#         # for i,j in enumerate(c):
#         #     print(i,j)
#         self.su.execute('select * from nine')
#         c=self.su.fetchall()
#         for i,j in enumerate(c):
#             print(i,j)
#
#
#             # print(self.su.fetchall())
#
#
#
#
# d = Mysql_learn()
# d.cao_zuo()


