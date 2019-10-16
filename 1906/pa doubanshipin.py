#!/usr/bin/python
#-*-coding:utf8-*-
import requests
import json
import time
import re
from time import sleep
i = 0
while i<=540:
    time.sleep(3)
    url='https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师kt=3&=0&_v=0.82849648&x-zp-page-request-id=4c7bca6ce5084c38990efccfa0d28eec-1569202318569-920432&x-zp-client-id=f275924e-8794-4884-ac47-29ad7a793e2a'.format(i)
    i+=90
    head ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/69.0'}
    html=requests.get(url,headers=head)
    geshi=html.text
    result=json .loads(geshi)





