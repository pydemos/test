#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen

class Animal:
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

dog1 =  Animal('西西 ',17)

print('name=%s'%dog1.name)
print('agee=%s'%dog1.age)

dog2= Animal('贝贝',33)

print('name=%s'%dog2.name)
print('agee=%s'%dog2.age)
