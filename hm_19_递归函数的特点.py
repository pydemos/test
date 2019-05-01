#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def sum_number(num):
    print(num)
    #递归的出口,当参数满足某个条件时,不在执行函数
    if num <=  1 :
        return
    sum_number(num -1 )

sum_number(3)
#函数调用自身的,编程技巧称为递归
# 特点. 一个函数内部调用自己
#函数内部可以调用其他函数,当然在函数内部也可以调用自己
#代码特点.1 函数内部的代码是相同的,只是针对参数的不同,处理结果的不同.
#2 当参数满足一个条件时,函数不在执行.这个非常重要,通常被称为递归函数的出口,否则会出现死循环