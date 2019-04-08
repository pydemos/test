#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
# 定义了一个类:完成对面积的计算
#定了一个类：完成对面积的计算
'''
class JuxingArea():
    def getNums(self):
        self.__a = int(input("请输入:"))
        self.__d = int(input("请输入:"))
    def cal(self):
        print('矩形的面积为%d'%self.__a*self.__b)
        #定义一个函数计算三角形的面积
class SanjiaoxingArea():
    def getNums(self):
        self.__a=int(input('请输入:'))
        self.__b=int(input('请输入:'))
    def cal(self):
        print("三角形的面积为%f"%(self.__a*self.__b/2.0))

a= SanjiaoxingArea()
a.getNums()
a.cal()
'''
class GetNum:
    def getNums(self):
        self.a = int(input("请输入:"))
        self.b = int(input("请输入:"))
class JuxingArea(GetNum):
    def cal(self):
        print('矩形的面积为%d'%(self.a*self.b))
class SanjiaoxingArea(GetNum):
    def cal(self):
        print("三角形的面积为%f"%(self.a*self.b/2.0))
a= SanjiaoxingArea()
a.getNums()
a.cal()

a= JuxingArea()
a.getNums()
a.cal()