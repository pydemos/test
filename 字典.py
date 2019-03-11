#! /usr/bin/env python
#coding=utf-8
#字典是一个无序的集合,使用print 函数输出字典时,
# 通常输出的顺序和定义的顺序是不一样的.
xiaoMing = {'name':'小明',
            'age':12,
            'address':'xiamen',
            'weight':34}
print(xiaoMing)
#字典的取值.如果key不存在报错
print(xiaoMing['name'])
#字典增加
xiaoMing['aff']=14
print(xiaoMing)
#修改.如果键在的话会被修改.如果键不在的会会被新增
xiaoMing['name']='wada'
print(xiaoMing)
#删除
xiaoMing.pop('address')
print(xiaoMing)
#字典的遍历
for i in xiaoMing :
    print('%s : %s' %(i,xiaoMing[i]))