#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class f1:
    pass
class s1(f1):
    def show(self):
        print('s1 home')
class s2(f1):
    def show(self):
        print('s2.show')
def Fun(obj):
    print(obj.show())

s1_obj = s1()
Fun(s1_obj)

s2_obj = s2()
Fun(s2_obj)