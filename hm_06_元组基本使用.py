#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
info_tuple =('zhangsan',10,1.75,'zhangsan')
#1取值和取索引
print(info_tuple[0])
#已经知道数据的内容,希望知道数据在元组中的索引
print(info_tuple.index('zhangsan'))
#2.统计计数
print(info_tuple.count('zhangsan'))