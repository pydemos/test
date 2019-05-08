#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat:
    def __init__(self,new_name):
        self.name = new_name
    def eat(self):
        print('%s 在吃东西'%self.name)
    def drink(self):
        print('%s 正在喝水'%self.name)

Tom = Cat('haha')
Tom.eat()
Tom.drink()