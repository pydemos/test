#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
hello_str = 'hello hello'
#len 查看字符串的长度
print(len(hello_str))
#查看字符串中某个元素出现的次数
print(hello_str.count("h"))
#index和find的区别.index查不到会报错,find返回负一
#print(hello_str.index('bal'))
print(hello_str.find('bal'))
#字符串中的转义符
#\n 换行符 \r 回车 \' 单引号  \"双引号.