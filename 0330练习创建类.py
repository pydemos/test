#! /usr/bin/env python
#coding=utf-8
import  time
class Gun():
    #属性
    color = '黑色'
    #方法
    def setName(self,newName):
        self.name = newName
    def setBulletNum(self,num):
        self.__bulletnum = num
    def setJianBullNum(self,num):
        self.__jianbullernum = num
    def biubiu(self):
        self.__bulletnum= self.__bulletnum-self.__jianbullernum
        print('剩余的子弹数为%s'%self.__bulletnum)
ak = Gun()
ak.setName('AK45')
ak.setBulletNum(100)
ak.setJianBullNum(4)



ak.biubiu()
time.sleep(2)
ak.biubiu()