#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#定义一个函数sum_numbers
#能够接收一个num的整数参数
#计算1+2+3+4+num 的结果
def sum_numbers(num):
    #1.出口
    if num ==1 :
        return 1
    #2数字的累加num+ (1...num-1)
    temp = sum_numbers(num-1)
    return  num +temp
result = sum_numbers(3)
print(result)