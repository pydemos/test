#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def demo (num,numlist):
    print('函数内部的代码')
    num =100
    numlist=[1,2,3]
    print(num)
    print(numlist)
    print('函数执行完成')
gl_num = 99
gl_list = [4,5,6]
demo(gl_num ,gl_list)
print(gl_num)
print(gl_list)
#可变和不可变的参数 ,问题1 在函数内部,针对参数使用赋值语句,会不会影响调用函数时传递的实参变量??
#--不会  无论传递的是参数是可变还是不可变的
#只有针对参数使用赋值语句,在函数内部修改局部变量的引用,不会影响到外部变量的引用