#! /usr/bin/env python
#coding=utf-8
import cards_tools
while True:
    #TODO (小明:显示功能菜单)
    cards_tools. new_card()
    print('*'*50)
    print("欢迎您使用名片系统!")
    print('0退出名片系统!')
    print('1新建名片!')
    print('2显示名片!')
    print('3查询名片!')
    ation_str = str(input("请输入希望执行的操作:"))
    print("您选择的操作是[%s] }"%ation_str)
    #1.2.3针对名片的操作
    if ation_str in ['1','2','3']:
        pass
    elif ation_str == "1":
        print('')
    elif ation_str == "2":
        pass
    elif ation_str =="3":
        pass
    elif ation_str == "0" :
        print('欢迎您再次使用!')
        break
    else :
        print('你输入的不正确,请重新选择!')

