#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def demo (num_list):
    print('函数的内部代码')
    #使用方法修改列表的内容
    num_list.append(9)
    print(num_list)
    print('函数执行的完成')

gl_list = [1,2,3]
demo(gl_list)
print(gl_list)
#问题2 :如果传递的参数是可变函数,在函数的内部.使用方法修改了数据的内容.同样的会影响到外部的数据