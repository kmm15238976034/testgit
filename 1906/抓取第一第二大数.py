#!/usr/bin/python
#-*-coding:utf8-*-
# b=[]
# a=input('输入数字').split(',')
# for i in a:
#     i =int(i)
#     b.append(i)
#     b.sort()
#     b.reverse()
# print(b[0],b[1])
import requests
import re
# j = 0
# while j < 25:
a='http://www.wfsfnvp.com/book/7/7709/2481034.html'
# j+=1
b=requests.get(a)
c=b.content.decode('gbk')
q=re.compile('</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">style6()',re.S)
w=q.findall(c)
for i in w:
    for j in i:
        j=j.replace('<br />',' ')
        j=j.replace('&nbsp;&nbsp;&nbsp;&nbsp;',' ')
        with open('hunli.txt','a',encoding='utf-8')as x:
            x.write(j)
    # for i in w:
    #     i=i.replace('<p>',' ')
    #     i=i.replace('</p>',' ')
    #     print(i)


   `