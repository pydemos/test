#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#假设以下内容是刚从网络上抓取的
#要求.1将字符串的空白字符全部去掉
#2 再将""作为分隔符,拼接成一个整齐的字符串
poem_Str = "等请热热\t  王之涣  \t 白日依山尽 \t  \n 黄河入海流 \t \n"
print(poem_Str)
poem_List = poem_Str.split()
print(poem_List)
result =" " .join(poem_List)
print(result)
a = "hello" + "python"
print(a)
b=(1,2)+(2,3)
print(b)
t_list = [1,2]
t_list.extend([5,6])#合并到当前的列表中
print(t_list)
t_list.append(9)
print(t_list)
t_list.append([6,7])
print( t_list )#追到末尾生成独立的元素