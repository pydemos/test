#! /usr/bin/env python
#coding=utf-8
import  time
class Gun():
    #属性
    color = '黑色'
    #方法
    def __init__(self,newName,allnum,num):
        self.__name = newName
        self.__num= allnum


    def setName(self,newName):
        self.name = newName
    def setBulletNum(self,allnum):
        self.__bulletnum = allnum
    def setJianBullNum(self,num):
        self.__jianbullernum = num
    def biubiu(self):
        if self.__bulletnum > self.__bulletnum:
            self.__bulletnum = self.__bulletnum-self.__jianbullernum
        else:
            self.__bulletnum = 0
            print('剩余的子弹数为%s'%(self.__name,self.__bulletnum))
ak = Gun('ak14',100,4)
# ak.setName('AK45')
# ak.setBulletNum(100)
# ak.setJianBullNum(4)

mp5= Gun()
mp5.setName('AK45')
mp5.setBulletNum(100)
mp5.setJianBullNum(4)
while True:

    mp5.biubiu()
    time.sleep(2)
    mp5.biubiu()