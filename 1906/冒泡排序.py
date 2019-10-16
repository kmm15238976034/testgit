#!/usr/bin/python
#-*-coding:utf8-*-b
#九九乘
# 法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i, j, i * j), end=' ')
#     print()
#质数之和
# a=int(input('值1'))
# b=int(input('值2'))
# sum=0
# for i in range(a,b+1):
#     k=2
#     if i>=2:
#         while i % k!=0:
#             k+=1
#     if i==k:
#         sum+=i
#     print(sum)
#阶乘之和
# a=int(input('值1'))
# sum=0
# for i in range(1,a+1):
#     a=1
#     for j in range(1,i+1):
#         a=a*j
#     sum+=a
# print(sum)
#判断三角形
# a=int(input('输入第一条边'))
# b=int(input('输入第二条边'))
# c=int(input('输入第三条边'))
# n= [a,b,c]
# n.sort()
# if n[0]+n[1]>n[2]:
#     if n[0]**2+n[1]**2>n[2]**2:
#         print('是锐角三角形')
#     elif n[0]**2+n[1]**2==n[2]**2:
#         print('是直角三角形')
#     elif n[0]**2+n[1]**2<n[2]**2:
#         print('是钝角三角形')
# else:
#     print('不是三角型')
#判断以什么开头以什么结尾
# a=input('一个国家')
# if a.startswith('我')and a.endswith('你'):
#     print('hao')
# else:
#     print('nihao')
#判断字符串是否回文
# def huiwen(*args):
#     a=args
#     b=a[::-1]
#     if a==b:
#         print('回文')
#     else:
#         print('不回文')
# huiwen(123321)
                        # 函数方法：
                        # a=input('输入')
                        # c=[]
                        # for j in a[::-1]:           #代表从最后一个开始
                        #     c.append(j)
                        #     if list(a)==c:
                        #         print("回文")
                        #         break
                        # else:
                        #     print("不回文")
# while True:
#     a=input('输入字符串')
#     c=list(a)
#     b=list(reversed(c))
#     if b==c:
#         print('回文')
#     else:
#         print('不是回文')

#排序（选择冒泡）

#冒泡排序
# a=[1,3,2,4]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]>a[j+1]:
#             a[i],a[j+1]=a[j+1],a[i]
# print(a)


#选择排序
# b=[1,2,4,3]
# for i in range(0,len(b)):
#     for j in range(i+1,len(b)):
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
# print(b)

#三次猜数字
# import random
# a=random.randrange(6)
# for i in range(3):
#     b=input('请输入大/小')
#     if b=='大':
#         if 0 <a<=3:
#             print('错了'.format(2-i))
#         elif 3<a<=6:
#             print('对了')
#             break
#     elif b=='小':
#         if 0<a<=3:
#             print('对了')
#             break
#         elif 3<a<=6:
#             print('错了'.format(2-i))
#     else:
#         print('请重新输入')

# #水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)
#打印列表里第一大数和第二大数
# a=[2,3,4,2,4,3,2]
# a.sort()
# a.reverse()
# b=[]
# c=[]
# d=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# c.append(b[0])
# c.append(b[1])
# for j in a:
#     if j in c:
#         print(j,end=' ')

#不用int将字符串转换为整数
# a='1234'
# a=a[::-1]
# print(a)
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b+=j*10**i
# print(b)
#任意4个数，组成不同的三位数。
# a=input('>>>')
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=j !=k:
#                 print(i,j,k)
#
#
# q=int(input('>>1>>'))
# w=int(input('>>2>>'))
# e=int(input('>>3>>'))
# r=int(input('>>4>>'))
# t=[q,w,e,r]
# a=[]
# for i in range(1,len(t)+1):
#     for j in range(1,len(t)+1):
#         for k in range(1,len(t)+1):
#             if i !=j and i!=k and j !=k:
#                 b=i**100+j*10+k
#                 if b not in a:
#                     a.append(b)
# print(a )

#将列表里的元素向左挪一位
# a=[4,2,5,6]
# for i in range(len(a)-3):
#     a.insert(len(a),a[0])
#     a.remove(a[0])
#     print(a)


#十进制数转换成十六进制
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

#因数求和
# sum=0
# a=int(input('请输入值'))
# for i in range(1,a+1):
#     if a%i == 0:
#         sum+=i
# print(sum)

#一个数的因数之和等于它本身
# a=int(input('请输入数字'))
# b=[]
# for i in range(1,a):
#     if a%i==0:
#         b.append(i)
# d=sum(b)
# if d==a:
#     print(a)
# else:
#     print('不相等')

#将列表中最大的数放在最大的放在最后一位，最小的放在第一位（不改变结构）
# a=[5,3,2,6,7]
# c=max(a)
# d=min(a)
# a.remove(c)
# a.remove(d)
# a.insert(0,d)
# a.insert(len(a),c)
# print(a)


# import copy
# a=[14,35,23,4,32,22]
# b=a.copy()
# c=[]
# a.sort()
# for i in a:
#     if i==a[0] or i==a[-1]:
#         c.append(i)
#         b.remove(i)
# b.insert(0,c[0])
# b.append(c[1])
# print(b)

#一个有顺序的列表，随机加入一个数，加入的数在正确的位置\
# a=[6,2,3,7,1]
# b=int(input('输入值'))
# a.append(b)
# a.sort()
# print(a)

#用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# for i in range(0,51):
#     for j in range(0,101):
#         for k in range(0,101):
#             if i+j+k==100 and 2*i+j+0.5*k==100:
#                 a='公鸡：{},母鸡：{}，小鸡：{}'.format(i,j,k)
#                 print(a)


#一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# def hanshu(b,*a):
#     c=[]
#     for i in a:
#         for j in a:
#             if i+j==b and i !=j:
#                 c.append(i)
#                 if j not in c:
#                     if i+j==b and i!=j:
#                         print(i,j)
# hanshu(14,23,11,13,27)




