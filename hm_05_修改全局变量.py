#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
num =  10
def demo1 ():
    #希望修改全局变量的值 --使用global 声明一下变量即可
    #gobal 关键字会告诉解释器后面的变量是一个全局变量
    #在使用赋值语句时候,就不会在创建局部变量.
    global  num
    num = 30

    print('demo1 ==>%d'%num)

def demo2():
    num= 130
    print('demo2 ===>%d'%num)
demo1()
demo2()