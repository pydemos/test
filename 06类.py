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
    def __setName(self,newName):
        self.name  = newName
        self.__money = 100
    def newSetName(self,newName):
        self.__setName(newName)
    def showMoney(self):
        print('%s 还剩下这么多钱'%self.__money)
    def run(self):
        print('%s狗狗正在跑'%self.name)
    def eat(self):
        print('%s 狗狗正在吃'%self.name)
jinMao = Dog()
jinMao.newSetName('haha')

