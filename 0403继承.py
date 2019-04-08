#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat :
    #属性
    color = 'black'
    legs = 4
    weight = 6
    #方法
    def miaomiao(self):
        print('猫在喵喵叫..')
    def catch(self):
        print('抓老鼠')
#子类
class Bosi(Cat):
        def naoyangyang(self):
            print('1232a')
    #属性
class Tomcat(Bosi):

    pass

bosi = Bosi()
bosi.miaomiao()
bosi.catch()
bosi.naoyangyang()