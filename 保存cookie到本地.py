#! /usr/bin/env python
#coding=utf-8
#admin
from urllib import  request
from http.cookiejar import  MozillaCookieJar
cookiejar = MozillaCookieJar('cookie.tet')
cookiejar.load (ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://httpbin.org/cookies/set?course-abc')
cookiejar.save(ignore_discard=True)#(设置cookie是否过期)
for cookie in cookiejar:
    print(cookie)