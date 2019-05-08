#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat():
    def __init__(self,new_name):
        self.name = new_name
    def eat(self):
        print('%s  在吃鱼'%self.name)
tom = Cat('pipi')
tom.eat()

dog = Cat('gougou')
dog.eat()

'''
初始化方法
当使用类名()创建对象时,会自动执行以下操作:
1.为对象在内存的使用,分配空间--创建对象
2.为对象的属性设置初始值--初始化方法
这个初始化方法就是__init__方法,__init__是对象的内置方法
4.3 在初始化方法的内部定义属性
在__init__方法内部使用self.属性名 = 属性的初始值.就可以定义属性
定义属性之后,在使用Cat 类创建的对象,都会拥有该属性



'''