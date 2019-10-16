#!/usr/bin/python
#-*-coding:utf8-*-
a=int(input('输入值a'))
b=int(input('输入值b'))
sum=0
for i in range(a,b+1):
    k=2
    if i>=2:
        while i % k !=0:
            k +=1
    if i==k:
        sum += i
print(sum)
# a=int(input('值1'))
# b=int(input('值2'))
# sum=0
# for i in range(a,b+1):
#     k=2
#     if i>=2:
#         while i%k!=0:
#             k+=1
#         if i==k:
#             sum+=1
# print(sum)

