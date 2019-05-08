#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return  '[%s]占地 %2.f'%(self.name,self.area)
#1创建家居
bed  = HouseItem('席梦思',4)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',3)
print(bed)
print(chest)
print(table)