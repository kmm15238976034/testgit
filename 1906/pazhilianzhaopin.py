#!/usr/bin/python
#-*-coding:utf8-*-
import requests
import json
import time
import xlwt
xr=xlwt.Workbook(encoding='utf-8')
sheet=xr.add_sheet('gongsi')
a='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.58872527&x-zp-page-request-id=666f887f8140431294135b0de2ced21b-1569230708860-929622&x-zp-client-id=f275924e-8794-4884-ac47-29ad7a793e2a'
bianliang={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
b=requests.get(a,headers=bianliang)
c=b.text
a=json.loads(c)
print(a)
s = a['data']['results']
for i in range(90):
    name=a['data']['results'][i]['company']['name']
    print(name)
    sheet.write(0,1 ,name)
