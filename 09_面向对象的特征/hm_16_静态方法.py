#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Dog(object):
    def run(self):
        #不访问实例属性/类属性
        print('Dog 要跑')
    #通过类名.调用静态方法 .
Dog.run()
