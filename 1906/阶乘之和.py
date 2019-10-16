#!/usr/bin/python
#-*-coding:utf8-*-
a = int(input('请输入值'))
sum = 0
for i in range(1,a+1):
    a = 1
    for j in range(1,i+1):
        a = a*j
    sum = sum + a
print(sum)
