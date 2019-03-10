#! /usr/bin/env python
# coding=utf-8
# 223.99.197.253	63000
from urllib import request
#不使用代理
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
# print(resp.read())
#使用代理
#1.使用proxyiHandler，传入代理构建一个handler
handler = request.ProxyHandler({'http':'113.13.160.100:9999'})
#2.使用上面创建的handlor构建一个opener
opener = request.build_opener(handler)
#3.使用opener去发送个请求
resp= opener.open('http://httpbin.org/ip')
print(resp.read())
