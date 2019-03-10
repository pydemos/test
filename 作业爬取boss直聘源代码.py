#! /usr/bin/env python
#coding=utf-8
from urllib import  request
from urllib import  parse

url='https://www.zhipin.com/'
headers = {
'User-Agent':'Mozila/5.0 (Windows NT 10.0; WOW64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/63.0.3239.132 Safari/537.36'
'Referer:https://www.baidu.com/link?url=EIihfXsUtrrC-g_ZP4g22xl-emcWFhtCqLv9mPwbJ9z40_ohsUECO3vxdUDdhl27&wd=&eqid=f6461e370002d3a0000000065c4d850f'
}
data={
    'first':'ture',
    'pn':1,
    'kd':'python'
}
handler = request.ProxyHandler({'http':'113.13.160.100:9999'})
opener = request.build_opener(handler)

# req = request.Request(url,headers=headers,
#                       data=parse.urlencode(data).encode('utf-8')
#             )
resp = request.urlopen(url)
print(resp.read().decode('utf-8'))