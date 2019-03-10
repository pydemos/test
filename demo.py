#! /usr/bin/env python
#coding=utf-8
import  requests
from lxml import  etree
#1将目标网站的页面抓取下来
headers = { 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/63.0.3239.132 Safari/537.36",
    'Referer': 'https://movie.douban.com/'}
response = requests.get('http://www.baidu.com',headers=headers)

