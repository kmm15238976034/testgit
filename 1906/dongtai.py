#!/usr/bin/python
#-*-coding:utf8-*-
# import json
# a=json.loads('{"result":{"data":12}}')
# print(a['result'][])


# import requests
# import json
# with open('111.txt','w',encoding='utf-8')as f:
#     url='https://map.baidu.com/?qt=subwayscity&t=1569033419320'
#     html=requests.get(url)
#     geshi=html.text
#     result=json.loads(geshi)
#     i=0
#     while True:
#         try:
#             city = result['subways_city']['cities'][i]['cn_name']
#             f.write(city+'/n')
#             print(city)
#             i+=1
#         except:
#             break


def hanshu(a,b):
    c=a+b
    print(c)