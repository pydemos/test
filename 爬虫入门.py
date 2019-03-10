#! /usr/bin/env python
#coding=utf-8
from urllib import  request
from urllib import  parse
#1 urlopen的用法
#1resp = request.urlopen('http://ww.baidu.com)#查看网页的源代码
#1print(resp.readlines())
#2 urlretrieve的用法
#2request.urlretrieve('http;//www.baidu.com','baidu.html')#静态的网页数据另存到本地
#3urlencode的用法
#url = 'https://www.baidu.com/s?wd=%E5%88%98%E5%BE%B7%E5%8D%8E&ie=UTF-8'#百度刘德华源码
# url = 'https://www.baidu.com/s?wd'
# params = {'':'刘德华'}
# name = parse.urlencode(params)
# print(url+name )
# params = {'name':'张三','age':18,'greet':'hello world'}
# qs = parse.urlencode(params)
# print(qs)#转码后
# result = parse.parse_qs(qs)
# print(result)#转回码
#4  urlparse 和urlsplit . urlparse 没有params这个参数
# url = 'http://www.baidu.com/s?wd=python&username=abc#1'
# result = parse.urlparse(url)
# result1 = parse.urlsplit(url)
# print(result1)
# print('soheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path:',result.path)
# print('params:',result.params)
# print('query:',result.path)
# print('fragment:',result.fragment)

