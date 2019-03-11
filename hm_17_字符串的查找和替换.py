#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
hello_str = 'hello hello'
print(hello_str.startswith('hell'))
print(hello_str.endswith('o'))
print(hello_str.find('o'))
#replace 方法执行完成够,会返回一个新的字符串
# ,字符串元素中相同的元素都会被替换
#注意:不会修改原有字符串的内容
print(hello_str.replace('llo', 'p'))
print(hello_str)
