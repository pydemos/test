#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
'''
需求:
1在Do g类中封装方法game
普通狗只是简单的玩耍
2定义XiaoTianDog继承自Dog,并且重写game方法
哮天犬需要在天上玩耍
3定义Person 类.并且封装一个和狗玩的方法
在方法内部直接让狗对象调用game方法
'''
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print('%s 蹦蹦跳跳的玩耍...'%self.name)
class XiaoTianDog(Dog):
    def game(self):
        print('%s 飞到天天上去 '%self.name)
class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print('%s 和 %s  快乐的玩耍...'%(self.name,dog.name))
        dog.game()

#1创建狗对象
wangcai=Dog('旺财')
#2创建一个小明对象
xiaoming=Person('小明')
#3让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)