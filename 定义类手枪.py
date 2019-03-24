#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Dog():
    color = '白色'
    sex = "公"

    def setName(self, newName):
        self.name = newName


    '''
    def setjinmao(self):
        self.name = '小白'

    def sethashiqi(self):
        self.name = '哈士奇'

    def setzangao(self):
        self.name = '藏獒'
    '''


    def eat(self):
        print('%s在吃骨头' % self.name)


    def run(self):
        print('%s正在跑' % self.name)


# jinMao = Dog()
# jinMao.setjinmao()
# jinMao.run()
#
# hashiqi = Dog()
# hashiqi.sethashiqi()
# hashiqi.run()
#
# zangAo = Dog()
# zangAo.setzangao()
# zangAo.eat()

jinMao = Dog()
jinMao.setName('金毛')
jinMao.run()

hashiqi = Dog()
hashiqi.setName('哈士奇')
hashiqi.run()

zangAo = Dog()
zangAo.setName('藏獒')
zangAo.eat()
