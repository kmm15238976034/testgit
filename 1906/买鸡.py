#!/usr/bin/python
#-*-coding:utf8-*-

for i in range(0,50):
    for j in range(0,101):
        for k in range(0,101):
            if i+j+k==100 and 2*i+j+0.5*k==100:
                a='公鸡：{},母鸡：{}，小鸡：{}'.format(i,j,k)
                print(a)


