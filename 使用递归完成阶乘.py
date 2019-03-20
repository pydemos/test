#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#用递归的方式实现累积和
#递归就是一个函数调用它自己,切记,一定要有结束调用它自己的时候
#否则程序在调用自己很多次之后,会崩溃
def test(num):
    i = 1
    sumResult =0
    while i <= num:
        sumResult = sumResult + i
        i += 1
    return  sumResult
def test2(num):
    if num >= 1:
        result = num+test2(num-1)
    else :
        result=0
    return result
def test3(num):
    if num >=1:
        result2 = num *test3(num-1)
    else:
        result2=1
    return  result2

#   100+(1+2+3+'''99)
result = test3(4)
print(result)
result = test2(100)
print(result)
result = test(100)
print(result)