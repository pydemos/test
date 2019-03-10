#! /usr/bin/env python
#coding=utf-8
#要求模拟浏览器headers返回用户的数据.越多越好
from  urllib import  request
from  urllib import  parse
url='https://www.lagou.com/jobs/list_pyhton?labelWords=&fromSearch=true&suginput='
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
             'AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/63.0.3239.132 Safari/537.36'
             'Referer:https://www.lagou.com/jobs/list_pyhton?labelWords=&fromSearch=true&suginput='
}
data={
    'first':'ture',
    'pn':1,
    'kd':'python'
}
req = request.Request(url,headers=headers,
                      data=parse.urlencode(data).encode('utf-8'),
                      method='POST')
resp=request.urlopen(req)
print(resp.read().decode('utf-8'))