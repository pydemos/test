#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
'''
soldier     Gun
name       model
gun        bullet_count
__init__self()   __init__(self,model ):
fire(self)    shoot(self):
'''
class Gun:
    def __init__(self ,model):
        #1枪的型号
        self.model = model
        #2子弹的数量
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        #1判断子弹的数量
        if self.bullet_count<=0:
            print('[%s]没有子弹了...'%self.model)
            return
        # 2发射子弹,-1
        self.bullet_count -=1
        #3提示发射信息
        print('[%s] 突突突突..[%d]'%(self.model,self.bullet_count))

class Soldier:
    def __init__(self,name):
        #1.姓名
        self.name = name
        #2.枪 -新兵没有枪
        self.gun = None
    def fier (self):
        #1.判断士兵是否有枪
        if self.gun ==None:
            print('[%s ]还没有枪...'%self.name)
            return
        #2.高喊口号
        print('冲阿...[%s]'%self.name)
        #3.让枪装填子弹
        self.gun.add_bullet(50)
        #4.让枪发射子弹
        self.gun.shoot()
#1创建枪对象
ak47  =Gun('AK47')


#2创建许三多
xusanduo = Soldier('许三多')
xusanduo.gun = ak47
xusanduo.fier()
print(xusanduo.gun)