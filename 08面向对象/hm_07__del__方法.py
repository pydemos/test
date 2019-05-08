#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print('%s 我来了'%self.name)
    def __del__(self):
        print('%s我去了'%self.name)
#tom 是一个全局变量
tom = Cat('Tom')
print(tom.name)
#del 关键字可以删除一个对象
del tom
print('-'*50)
'''
应用的场景 
__init__改造初始化方法.可以让创建对象更加灵活
__del__ 如果希望在对象被销毁前 ,可以考虑一下,__del__方法
生命周期
一个对象从调用 类名()创建,生命周期结束
一个对象的__del__方法一旦被调用,生命周期结束
在对象的生命周期内.可以访问对象属性,或者让对象调用方法

'''