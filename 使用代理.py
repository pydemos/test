#! /usr/bin/env python
#coding=utf-8
import  requests
proxy = {
    'http':'115.151.7.60:9999'
}
response = requests.get('http://httpbin.org/ip',proxies=proxy)
print(response.text)

import  requests
response = requests.get('http://www.baidu.com/')
print(response.cookies.get_dict())
