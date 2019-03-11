#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#要求,顺序并且居中对齐输入以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        '黄河入海流',
        "欲穷千里目",
        "更上一层楼"]
#居中对齐
for i in poem :
    print('|%s|'%i.center(10, ' '))
#向左对齐
for i in poem:
    print('|%s|' % i.ljust(10, ' '))
# 去除空白的字符,并且居中显示
poem = ["\t \n 登鹳雀楼",
        "王之涣",
        "白日依山尽\t \n",
        '黄河入海流',
        "欲穷千里目",
        "更上一层楼"]
for pe in poem :
    print('|%s|'%pe.strip().center(10, ' '))
