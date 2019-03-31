#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
import time


class Gun():
    # 属性
    color = '黑色'

    def __init__(self, newName, allNum, evNum):
        self.__name = newName
        self.__bulletnum = allNum
        self.__jianbulletnum = evNum

    # def setName(self, newName):
    #     self.__name = newName
    #
    # # 方法
    # # 设置枪的子弹数量
    # def setBulletNum(self, num):
    #     self.__bulletnum = num
    #
    # # 设定一个属性.表示每次开枪射出去的子弹数
    # def sefJianBulletNum(self, num):
    #     self.__jianbulletnum = num
    # 开枪.然后计算子弹数量
    def biubiu(self):
        if self.__bulletnum > self.__jianbulletnum:
            self.__bulletnum = self.__bulletnum - self.__jianbulletnum
        else:
            self.__bulletnum = 0

        print("%s 剩余的子弹数量为:%d" % (self.__name, self.__bulletnum))


AK47 = Gun('AK47', 100, 4)
# AK47.setName('AK47')
# AK47.setBulletNum(100)
# AK47.sefJianBulletNum(4)
#
mp5 = Gun('mp5', 32, 2)
# mp5.setName('AK47')
# mp5.setBulletNum(100)
# mp5.sefJianBulletNum(5)
while True:
    AK47.biubiu()
    mp5.biubiu()
    time.sleep(2)
    AK47.biubiu()
    mp5.biubiu()
