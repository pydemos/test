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
class Dog():
    def run(self):
        print('跑步')
    def drink(self):
        print('喝')
    def sleep(self):
        print('睡')
    def bark (self):
        print('叫')
wangcai  = Dog()
wangcai.drink()
wangcai.run()
wangcai.bark()
'''
子类继承自父类,可以直接享受父类中已经封装好的方法,不需要再次开发
子类中应该根据职责,封装子类特有的属性和方法
Dog 类是Animal 类的子类,Animal 类是Dog 类的父类.Dog 类从animal 类继承
Dog 类是animal类的派生类,Animal类是Dog类的基类,Dog类从animal类派生
'''