#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#子弹
class Zidan():
    def __init__(self,shashangli):
        self.shashangli = shashangli
    def gongjizhi(self):
        return self.shashangli()
 #弹夹

class Danjia:
    def  __init__(self, rongliang):
        self.danjiarongliang = rongliang
        self.zidanliebiao = []
    def zhuangzidan(self,zidan):
        self.zidanliebiao.append(zidan)
        print('子弹+1......当前的子弹数是:%d'%len(self.zidanliebiao))
    def chuzidan(self):
        if len(self.zidanliebiao) >0:
            zidan = self.zidanliebiao[-1]
            shashangli=zidan.gongjizhi()
            self.zidanliebiao.pop()
            print('子弹-1.....当前的子弹数是:%d'%len(self.zidanlieibiao))
        else:
            shashangli = 0
        return  shashangli

#枪
class Qiang:
    def __init__(self, name):
        self.name = name
    def huandanjia(self,danjia):
        self.danjia = danjia
    def fashe(self,mubiao):
        shashangli = self.danjia.chuzidan()
        mubiao.diaoxue(shashangli)

#人
class Ren:
    def __init__(self):
        self.shengmingzhi = 100
    def maiqiang(self, qiang):
        self.qiang = qiang
        print('买了一把枪')

    def yazidan(self, danjia, zidan):
        danjia.zhuangzidan(zidan)
    def zhuangdanjia(self,danjia):
        self.qiang.huandanjia(danjia)
    def kaiqiang(self,mubiao):
        self.qiang.fashe(mubiao)

    def diaoxue(self, shashangli):
        self.shengmingzhi -= shashangli
        print('剩余的生命值为%d'%self.shengmingzhi)
#创建了小明
xiaoming = Ren()
#创建了一把枪
daju = Qiang('daju')
#把对象(daju)当做一个参数.赋值给另外一个对象的属性
xiaoming.maiqiang(daju)
#创建弹夹
danjia = Danjia(100)

#创建一颗子弹
zidan = Zidan(5)

# 小明这个对象，把一颗子弹压到一个弹夹中
xiaoming.yazidan(danjia,zidan)
# 把弹夹安装到枪上，即把弹夹当做一个参数，传给给了枪
xiaoming.zhuangdanjia(danjia)
# 创建了一个人对象（老王）
laowang = Ren()
#创建一颗子弹
zidan = Zidan(10)
#把小明这个对象,把一颗子弹压到一个弹夹中
xiaoming.kaiqiang(danjia,zidan)
xiaoming.kaiqiang(laowang)
xiaoming.kaiqiang(laowang)
xiaoming.kaiqiang(laowang)
