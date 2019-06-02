#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class A:
    def test(self):
        print('A---test 方法')
    def demo(self):
        print('demo方法')
class B:
    def demo(self):
        print('demo方法')
    def test(self):
        print('B---test 方法')
class C(A,B):
    #多继承可以让子类的对象,同事具有多个父类的属性和方法
    print('jicheng ')
c =C()
c.test()
c.demo()
'''如果不同的父类中存在同名的方法,子类对象在调用方法是,,会调用哪个父类中的方法呢?
提示:在开发中,应该尽量避免这种容易产生混淆的情况,--如果父类之间存在同名的属性和方法,
应该尽量避免使用多继承'''
#确定C类
# + 对象的调用顺序
print(C.__mro__)