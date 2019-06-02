#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class A:
    def test(self):
        print('test 方法')
class B:
    def demo(self):
        print('demo方法')
class C(A,B):
    #多继承可以让子类的对象,同事具有多个父类的属性和方法
    print('jicheng ')


c =C()
c.test()
c.demo()