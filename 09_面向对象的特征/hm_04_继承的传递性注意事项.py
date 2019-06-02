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
class Cat(Animal):
    def catch(self):
        print('抓老鼠')
    def eat(self):
        print('wdwdwedwdw')
#创建一个哮天犬的对策
xtq = Cat()
xtq.eat()
xtq.catch()
#哮天犬不能调用,Cat中的catch方法因为哮天犬和cat 之间没有继承关系
'''
继承的传递性
C类从B类继承,B类又从A类继承 
那么C类就具有,B类和A类的所有方法和属性 
子类拥有的父类以及父类的父类中封装的所有的属性和方法
'''