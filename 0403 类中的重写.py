#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#定义一个猫类
class  Cat():
    #类析构
    def __init__(self,Newname,newAge):
        self.name = Newname
        self.age=newAge
        print('我是cat类中的构造方法')
class Bosi (Cat):#继承类
    #子类的方法名和父类的方法名相同
    def __init__(self,a,b,c):#在继承的基础上增加新的变量
        Cat.__init__(self,a,b)
        self.weght = c
        print('我是波斯类中的构造方法')
bosi=   Bosi('aaa',100,66)
print(bosi.name)
print(bosi.age)
print(bosi.weght)
