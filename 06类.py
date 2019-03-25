#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#类:是实实在在的对象,看得见摸得着的.先有类才有对象.一个模板.一张图纸
'''
类由3个部分构成
类的名称:类名  (人)
类的属性:一组数据(身高,年龄)
类的方法:允许对进行操作的方法(行为)(跑,打架 )
'''
class Dog :
    color = '白色'
    sex = '公'
    def eat (self):
        print('狗在吃骨头')
    def run(self):
        print('狗在跑')

jinMao = Dog.d()
jinMao.eat()
jinMao.run()
hasiqi = Dog()
zangao = Dog()

