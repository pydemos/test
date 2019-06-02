#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class a:
    def __init__(self):
        self.num1= 100
        self.__num2 = 200
    def __test(self):
        print('私有方法 %d %d' %(self.num1,self.__num2))
class b(a):
    def demo(self):
        #1在子类的对象方法中.不能访问父类的私有属性
        #print('访问父类的私有属性%d ^self.__num2')
        #2调用父类的私有方法
        #self._test()
        pass
#创建一个子类的对象
B= b()
print(b)
#在外界不能直接访问对象的私有属性/调用私有方法
print(B.__num2)
b.test()
'''
私有属性,方法.是对象的隐私.不对外公开.外界以及的子类都不能直接访问
私有属性.方法通常用于做一些内部的事情
'''