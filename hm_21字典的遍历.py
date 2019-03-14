#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen

students ={'name':'张胜男'},{'name':'李四'},{'name':'张三'}
find_name  = '李t 四'
for stu_dict in students :
    print(stu_dict)
    if  stu_dict["name"] == find_name :
        print('找到了%s '% find_name)
        break
else :
    print("抱歉没有找到 %s"%find_name)
print('循环结束')