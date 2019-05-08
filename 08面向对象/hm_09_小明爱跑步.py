#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Proson:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return  '我的名字叫%s ，我的体重是%.2f kg' %(self.name,self.weight)
    def eat(self):
        print('%s 在吃东西'%self.name)
        self.weight +=1
    def run(self):
        print('%s 正在奔跑'%self.name)

xiaoming=Proson('小明',54)
xiaoming.__str__()
xiaoming.eat()
xiaoming.run()
print(xiaoming)