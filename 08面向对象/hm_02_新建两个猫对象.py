#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat :
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫爱喝水')
    #创建猫对象
tom = Cat()
tom.eat()
tom.drink()
#在创建一个对象
lazy_cat = Cat()
lazy_cat.drink()
lazy_cat.eat()
print(tom)
