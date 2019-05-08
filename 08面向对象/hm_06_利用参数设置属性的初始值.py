#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat:
    def __init__(self,new_name):
        print('这是一个初始化方法')
        # self.属性名 = 属性的初始值
        # self.name  = 'Tom'
        self.name = new_name
    def eat(self):
        print('%s在吃东西'%self.name)


Tom = Cat('Tom')
print(Tom.name)
Tom.eat