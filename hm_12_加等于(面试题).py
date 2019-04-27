#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def demo(num,num_list):
    print('函数的开始')
    num +=num
    #列表变量使用+ 不会做相加在赋值的操作做
    #针对数字和字符串,都是先相加在赋值.但是针对列表变量中,加等于,本质上是在调用列表的extend方法
    # 不会修改引用.
    num_list = num_list + num_list
    #本质上是在调用列表的extend方法
    # num_list += num_list
    # num_list.extend(num_list)

    print(num)#18
    print(num_list)
    print('函数完成')

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)

