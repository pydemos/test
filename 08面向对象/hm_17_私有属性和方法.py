#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Wonmen:
    def __init__(self,name):
        self.name = name
        self.__age = 18
    def __secret(self):
        #在对象的方法的内部是可以访问对象的私有属性
        print('%s 的年龄是%d'%(self.name,self.__age))
xiaofang = Wonmen('小芳')
#私有属性.在外界不能够直接被访问
#print(xiaofang.__age)
#私有方法,在外界不能够被直接访问
xiaofang.__secret()
'''
在实际开发中,对象的某些属性或者方法可能只希望在对象的内部被使用.而不希望在外部被访问
私有属性就是对象不希望公开的属性
私有方法就是对象不希望公开的方法

'''