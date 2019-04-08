#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
import  time
class Gun():
    color = '黑色'
    def setName (self,newName):
        self.setName = newName
    def zongzidan(self,zidang):
        self.zidansl = zidang
    def meicizidan(self,cizidang):
        self.cizhidan = cizidang
    def shengyu(self):
        shengyuzidan = self.zidansl - self.cizhidan
        print('剩余的子弹数量为%s'%shengyuzidan)

AK47 = Gun()
AK47.setName('ak47')
AK47.zongzidan(100)
AK47.meicizidan(2)

AK47.shengyu()
time.sleep(1)

AK47.shengyu()
