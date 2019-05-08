#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print('%s 我来了'%self.name)
    def __del__(self):
        print('%s我去了'%self.name)
    def __str__(self):
        #必须是返回一个字符串的
        return  '我是小猫%s' %self.name

#tom 是一个全局变量
tom = Cat('Tom')
print(tom)

class weight :
    def run(self):
        pass
    def eat(self):
        pass