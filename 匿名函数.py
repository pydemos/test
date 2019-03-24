#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#匿名 --- 没有名字的函数 lambda空格加上参数,然后冒号加上表达式.
def num(a,b):
    return a+b
num(2,3)
num=lambda   a,b :a+b
result = num(12,34)
print(result)

num1 = lambda  c,b:c+b
result1 = num(32,2)
print()


def calNum (a):
    return  a+10005*44/11+55
a=23
a=calNum(a)
print(a)

if (lambda a:a+10005*44/11+55/40)(5) >10:
   # (引入匿名函数 变量a:公式)(赋给变量a 的值)
    print(a)