#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def sum_numbers(*args):#(args)
    num = 0
    print(args)
    for i in  args:
        num+= i
    return  num
result = sum_numbers(1,2,3,4,5)#sun_numbers ((1,2,3,4,5))
print(result)
