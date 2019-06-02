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
        print('吃老鼠')
#创建一个哮天犬的对策
dog = Animal()
dog.eat()
xtq = Cat()
#如果子类中重写了父类的方法
#在使用子类对象调用方法时,会调用子类中的重写的方法
xtq.eat()
xtq.catch()

'''
重写父类的方法,有两种情况,
1覆盖父类的方法
2对父类方法进行扩展
覆盖父类的方法
1如果在开发中,父类的方法和子类的方法实现完全不同,就可以使用覆盖的方式,
在子类中重新编写父类的方法实现,具体的实现方式,就相当于在子类中重写的方法,而不在会调用
父类封装的方法
'''