#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
# 加密
def jiaMi():
    # 导入加密的文件名和密码
    fileName = input('请输入要加密的文件名:')
    # 密码输入
    while True:
        try:
            password = int(input('请输入一个数字作为密码:'))
            break
        except:
            print('please input number!!')
    # 打开文件
    fileWord = open(fileName, 'r+')
    num = fileName.rfind('.')
    # 进行名字修改
    newFileName = fileName[0:num] + '加密' + fileName[num:]
    # 防止独处内容过大,一部分一部分的读
    content = fileWord.read(1)
    # 打开一个新的文件
    newFile = open(newFileName, 'a+')
    i = 0
    while len(content) > 0:
        # 将变量转换成整数型
        contentInt = ord(content)
        newContentInt = contentInt + password  # 密码
        # 转换成字符
        c = chr(newContentInt)
        # 写入
        newFile.write(c)
        content = fileWord.read(1)
        i += 1
        # 关闭文件
        newFile.close()
        fileWord.close()
        # 解密


def jieMi:
    # 获取文件名和密码
    fileName = input('请输入要加密的文件名:')
    # 密码输入
    while True:
        try:
            password = int(input('请输入一个数字作为密码:'))
            break
        except:
            print('please input number!!')
    # 打开文件
    fileWord = open(fileName, 'r+')
    # 查找文件的后缀位置
    num = fileName.rfind('.')
    # 查找[加密]字样
    num1 = fileName.rfind('[')
    # 进行名字的修改
    newFileName = fileName[0:] + '[解密]' + fileName[num:]
    # 打开新的文件
    newFile = open(newFileName, 'a+')
    #防止读出内容过大,一部分一部分的读
    content = fileWord.read(1)
    i = 0
    while len(content) > 0:
        # 将变量转换成整型
        contentInt = ord(content)
        # 进行加密
        newContentInt = contentInt - password  # 密码
        # 转换成字符
        c = chr(newContentInt)
        # 写入

        newFile.write(c)
        content = fileWord.read(1)
        i += 1
        # 关闭文件
    newFile.close()
    fileWord.close()
#创建功能菜单
while True :
    #请用户输入想要的操作1-加密2-解密3-退出
    try:
        work = int(input('请输入想要的操作1-加密2-解密3-退出:'))
    except :
        print('输入错误')
        continue
        #d对每个操作进行判断
        if work ==1 :
            jiaMi()
            print('加密成功')
        elif work ==2:
            jieMi()
        elif word == 3:
            exit()
        else :
            print('输入错误')
