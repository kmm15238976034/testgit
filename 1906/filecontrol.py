#!/usr/bin/python
#-*-coding:utf8-*-
# import requests
# a='https://video.pearvideo.com/mp4/adshort/20190919/cont-1604362-14404880_adpkg-ad_hd.mp4'
# b=requests.get(a)
# '''接收响应内容第一种text'''
# c=b.text
# print(b)
# '''接收响应内容第二种content：以字节的方式接收'''
# d=b.content
# print(d)
# import re
# zifu='4qwe\nqwdQssd123we5'
# guolv=re.compile('q(.*?)e',re.S)
# answer=re.findall(guolv,zifu)
# answer1=guolv.findall(zifu)
# for i in answer:
# print(i.strip('<br />\r\n<br />\r\n')+'\n')
#
# with open('视频下载.mp4','wb') as f:
#     f.write(d)
# import requests
# import re
# a='http://www.quanshuwang.com/book/9/9055/9674701.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# q=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# w=q.findall(c)
# dd=[]
# for i in w:
#     print(i.strip('<br />\r\n<br />\r\n'+'\n'))
#with open('111.txt','w',encoding='utf-8')as f:
  #  for j in f:
 #       s.write(i.strip('<br')
# import requests
# a='http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg'
# b=requests.get(a)
# c=b.content
# with open('huohutupian.jpg','wb')as x:
#     x.write(c) '=--iio