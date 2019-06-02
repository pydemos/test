#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class A:
    def __init__(self):
        self.num1= 100
        self.__num2 = 200
    def __test(self):
        print('私有方法 %d %d' %(self.num1,self.__num2))
    def test(self):
        print('父类的共有方法')
        self.__test()

class B(A):
    def demo(self):
        #1在子类的对象方法中.不能访问父类的私有属性
        #print('访问父类的私有属性%d ^self.__num2')
        #2调用父类的私有方法
        #self._test()
        #3 访问父类的共有属性
        print('子类的方法%d'%self.num1)
        self.test()
        pass
#创建一个子类的对象
b= B()
print(b)
b.demo()
b.test()
#在外界不能直接访问对象的私有属性/调用私有方法
# print(B.__num2)
# b.test()
'''
父类的私有属性和私有方法
1子类对象不能在自己的方法内部.直接访问父类的私有属性或者私有方法
2子类的对象可以通过父类的共有属性和方法间接访问到私有属性或者私有方法
一.私有属性和方法是对象的隐私,不对外公开,外界以及子类都不能直接访问
二.私有属性.方法通常用于做一些内部的事情
'''