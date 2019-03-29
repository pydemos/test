#! /usr/bin/env python
#coding=utf-8
class Dog():
    color ='白色'
    sex =  '公'
    def setName(self,newName):
        self.name = newName
        self.__money = 1321#私有属性.必须在建立一个函数才能调用
    def showMoney(self):
        print('工资是%s'%self.__money)
    def run(self):
        print('%s 正在奔跑'%self.name)
    def eat(self):
        print('%s 正在吃骨头'%self.name)
jinMao = Dog()

jinMao.setName('金毛')
print(jinMao.color)
print(jinMao.sex)
print(jinMao.name)
jinMao.showMoney()