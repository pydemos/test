#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def  measure():
    '''测量温度和湿度'''
    print('测量开始..')
    temp = 39
    wetness = 50
    print('测量结束')
    #元组.可以包含多个数据.因此可以使用元组让函数一次返回多个值
    #如果函数返回的是元组的话,小括号类型可以省略
    return  (temp,wetness)
result = measure()
print('温度为%s  湿度为%s'%(result[0],result[1]))
#如果函数返回的是类型是元组,同时希望单独处理元组中的元素
#可以使用多个变量.一次性接收函数返回的结果
#注意使用多个变量接收结果时,变量的个数应该和元组的中的元素的个数保持一致
gl_temp ,gl_wetness = measure()
print(gl_temp ,gl_wetness)