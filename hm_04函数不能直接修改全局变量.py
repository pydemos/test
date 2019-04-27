#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
gl_num =  10
gl_tittle = '黑马程序员'
name = '王宇'
def demo1 ():
    #希望修改全局变量的值
    #在python 中不允许直接修改全局变量的值
    #如果使用复制语句,会在函数的内部定义一个局部函数
    #在函数内部,可以通过全局变量的引用获取对应的数据
    global  num
    num = 30

    print('demo1 ==>%d'%num)
    print('%s'% gl_tittle)
    print('%s'% name)
def demo2():
    print('demo2 ===>%d'%num)
demo1()
demo2()