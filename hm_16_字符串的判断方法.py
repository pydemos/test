#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#1判断空白字符串
space_str = '(43)'
print(space_str.isspace())
print(space_str.isalpha())
print(space_str.isdecimal())#（常用）只能判断单纯的数字
#isnumeric,isdigit比 isdecimal强大
print(space_str.isnumeric())#还能判断中文数字
space_str = '一千零一'
print(space_str.isdigit())#True, 还能uncode的字符