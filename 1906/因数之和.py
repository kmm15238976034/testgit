#!/usr/bin/python
#-*-coding:utf8-*-
# sum=0
# a=int(input('请输入值'))
# for i in range(1,a+1):
#     if a%i == 0:
#         sum+=i
# print(sum)

# a = open(r'C:\Users\kangmm\Pictures\3b292df5e0fe9925100bbe7e3fa85edf8db1719d.jpg','rb')
# b =a.read()
# print(b)
a = open('a.txt','w',encoding='utf-8')
for i in range(25):
    b='nihao\n'
    a.write(b)
a.close()
c=open('a.txt','r',encoding='utf-8')



