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
class Dog(Animal):
    def bark(self):
        print('汪汪叫')
class  Xiaotianquan(Dog):
    def fly(self):
        print('我会飞')
xtq = Xiaotianquan()
xtq.eat()
xtq.fly()
xtq.bark()
'''
继承的传递性
C类从B类继承,B类又从A类继承 
那么C类就具有,B类和A类的所有方法和属性 
子类拥有的父类以及父类的父类中封装的所有的属性和方法
'''