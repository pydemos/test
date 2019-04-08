#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
import random

needjiami = str(input('请输入要加密的文件名:'))
openwj = open(needjiami, 'r')
# 创建新的文件名
newnamedian = needjiami.find('.')
if newnamedian > 0:
    newnameqian = needjiami[:newnamedian]
    newnamehou = needjiami[newnamedian:]
newname = newnameqian + ['jiami'] + newnamehou

newwrite = open(newname, 'w')
content = openwj.read(1)
while len(content) > 0:
    newwrite.write(content)
    newwrite.write(str(random.randint(11, 99)))
    content = openwj.read()
openwj.close()
newwrite.close()
