#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def test(num):
    print('在函数的内部%d 对应的内存地址是%d'%(num,id(num)))
    #1>定义一个字符串变量
    result = 'hello'
    print('函数的返回数据的内存地址是%d'%id(result))
    #2将字符串变量返回
    return  result
#1 定义一个数字的变量
a = 10
#数据的地址本质上就是一个数字
print('a 变量保存数据的内存地址%d'%id(a))
#2调用test函数.本质上传递的是实参保存数据的引用..而不是实参保存的数据
test(a)