#!/usr/bin/python
#-*-coding:utf8-*-
a =[i for i in range(10)]+[chr(i)for i in range(97,103)]
print(a)
b = int(input('>>>'))
f =[]
while True:
    d=b%16
    b=b//16
    f.append(a[d])
    if b==0:
        break
f.reverse()
print(f)
