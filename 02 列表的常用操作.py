#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
name_list = ['zhangsan','lisi','wangwu','lisi']
#1取值和取索引
#list index out of range .列表索引超出范围
print(name_list[2])
#r知道数据的内容,想要确定,数据在列表中的位置,
#使用index,方法需要注意的如果传递的数据不在列表中.程序会报错
#print(name_list.index('lisi4'))
#2 修改
name_list[2]='www'
print(name_list)
#3添加
name_list.append('wangru')
print(name_list)
#4指定位置插入
name_list.insert(2,'qiqi')
print(name_list)
#5将另外一个列表的合并到第一个列表的后面
temp_list = ['wadaw','wafd']
name_list.extend(temp_list)
print(name_list)
#del在内存中删除变量,一般情况下建议使用remove.pop
del name_list[2]
#6pop(*) 删除指定下标的数据pop默认删除最后一个
# remove 删除列表指定的数据,del删除表格
# del name_list
# print(name_list)
name_list.pop(2)
print(name_list)
#clear 清空整个列表的内容.空表
# name_list.clear()
# print(name_list)
#列表中一共有多少元素
list_len =len(name_list)
print('列表中包含%d个元素'%list_len)
#count列表中某个元素出现的次数
count =name_list.count('lisi')
print('张三出现的%d次'%count)
#remove 删除第一个出现的元素
name_list.remove('lisi')
#列表的升序
name_list.sort
#列表的降序
name_list.sort(reverse=True)
#逆序
name_list.reverse()