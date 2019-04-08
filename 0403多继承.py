#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class  a():
    def test1(self):
        print('----test1-----')
    def test(self):
        print('----test in  a ----')
#定义一个父类
class  b():
    def test2(self):
        print('----test2-----')
    def test(self):
        print('---test in b---')
#定义一个子类.继承a,b
class  c(a,b):
    def test(self):
        print('---test in c --')
c= c()
c.test1()
c.test2()
c.test()