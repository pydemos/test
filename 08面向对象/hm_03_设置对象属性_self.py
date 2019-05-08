#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat :
    def eat(self):
        #哪个对象的调用的方法,self就是哪一个对象的引用
        print('%s爱吃鱼'%self.name)
    def drink(self):
        print('%s爱喝水'%self.name)
    #创建猫对象
tom = Cat()
#可以使用  .属性名  利用赋值语句就可以了
tom.name = 'tom'
tom.eat()
tom.drink()
lazy_cat  = Cat()
lazy_cat.name= 'mao'

lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)

# 哪个对象的调用的方法,self就是哪一个对象的引用
#在类封装的方法内部,self表示当前调用方法的对象自己
#调用方法时,程序员不需要传递self 的参数
#在方法的内部1 可以通过self访问对象的属性
            #2 也可以通过self.调用其他的对象方法