#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
gl_list = [6,3,8]
#默认按照升序排序
gl_list.sort()
#如果需要降序排序,需要reverse 参数
gl_list.sort(reverse=True)
print(gl_list)
#定义函数时可以给某个参数指定一个默认，具有默认值的参数，叫做缺省函数。
#调用函数时如果没有传入缺省函数的值，则函数内部使用定义函数时指定的参数默认值。
#函数的缺省参数将常见的值设置为参数的缺省值，从而简化函数的调用。
