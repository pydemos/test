#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Animal :
    def eat(self):
        print('吃东西')
    def run(self):
        print('跑步')
    def drink(self):
        print('喝')
    def sleep(self):
        print('睡')
#创建一个对象
class Dog(Animal):
    def dask(self):
       print('haha')
class xiaotianquan (Dog):
    def fly(self):
        print('我会飞')
#创建一个哮天犬的对象
xtq = xiaotianquan()
xtq.fly()
xtq.dask()
xtq.eat()
'''
继承的传递性
C类从B类继承,B类又从A类继承 
那么C类就具有,B类和A类的所有方法和属性 
子类拥有的父类以及父类的父类中封装的所有的属性和方法
'''