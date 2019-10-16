#!/usr/bin/python
#-*-coding:utf8-*-
goods = [
    ('电脑',1999),
    ('鼠标',10),
    ('游艇',20),
    ('美女',998)
         ]
shopping=[]
money=int(input('请输入资产'))
for index,i in enumerate(goods):
    print(index,i)
buy=input('请输入你要买的商品：')
buy=int(buy)
if buy < len(goods)and buy >=0:
    buy=goods
    if buy[1]<money:
        shopping.append(buy)
        money -=buy[1]
        print(shopping,money)


