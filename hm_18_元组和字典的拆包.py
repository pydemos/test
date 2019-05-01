#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def demo (*args ,**kwargs):
    print(args)
    print(kwargs)
    #元组变量和字典变量
gl_num = (1,2,3)
gl_dict = {'name':'小明','age':12}
#demo(gl_num,gl_dict)
#拆包语法
demo(*gl_num,*gl_dict)
demo(1,2,3,name='小明',age = 118 )
'''
再调用有多值函数时,如果希望
将一个元组变量,直接传给args
将一个字典变量,直接传递给kwargs
就可以使用拆包,简化参数的传递,拆包的方式是:
在元组变量增加一个*,字典变量前增加两个**
'''