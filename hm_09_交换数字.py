#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
'''
#解法1使用其他变量
a =100
b = 5
c = a
a = b
b = c

#解法2 不能使用其他的变量
a = 100
b =6
a = a+b
b = a-b
a = a-b
print('a的值为%d  ,b的值为%d'%(a,b))
'''
#解法3  python 专有
a =100
b = 3
#a,b =(b,a)
a,b= b,a#右边的为元组,只是去除了括号
print('a的值为%d  ,b的值为%d'%(a,b))