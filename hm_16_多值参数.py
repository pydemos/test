#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)
# demo(1,3,4)
# demo(1,2,3,4,5)
demo(1,23,443,43, name ='小明',age = 13)
#多值参数,   1 定义支持多值参数的函数
#有时可能需要一个函数能够处理的参数个数是不确定的,这个时候,就可以使用多值参数
#python 中有两种多值参数1 参数名前面增加一个* 可以接收元组
                        #2 参数名前面增加两个**可以接收字典
#一般在给多值参数命名时,习惯使用以下两个名字
# *args 存放元组参数,前面一个
#**kwargs  存放字典参数,前面有两个.
# args是arguments 的缩写 ,有变量的含义
# kw 是keyword的缩写kwargs 可以记忆键值对的参数
#提示:多值参数的应用会经常出现在网上一些大的框架中.
