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
    def bark(self):

#1如果子类中重写了父类的方法
        print('神一样的叫唤')
#2在使用子类对象调用方法时,会调用子类中的重写的方法
        #super().bark()
        #使用父类名.方法(self)
        Dog.bark(self)
        #Xiaotianquan.bark(self)
        #注意:如果使用子类的调用方法,会出现递归调用,--->死循环
#3增加其他子类的代码
        print('&&$(#@$@$)@_$@')
xtq  =Xiaotianquan()
xtq.bark()
xtq.eat()
xtq.fly()