#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#打开文件
'''
f = open ('121.txt','r')

content = f.readlines ()
while len(content)> 0:
    print(content)
    content = f.read(10 )
'''
f = open('121.txt','r')

content  = f.readlines()
while  len(content)>0 :
    content  = f.readlines()