#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
# 无限循环.由用户主动决定是否退出
import cards_tools

while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action_str = str(input('请选择你要执行的操作:'))
    print("您选择的操作是 [%s]" % action_str)

    # 1,2,3针对名片的操作.如果是其他的.提示操作错误
    if action_str in ["1", "2", "3"]:
        #1新增名片
        if action_str == "1":
            cards_tools.new_card()
        #2显示全部
        elif action_str == "2":
            cards_tools.show_all()
        #3查询名片
        elif action_str == "3":
            cards_tools.search_card()
        #0退出程序
    elif action_str == "0":
        print('欢迎您再次使用名片系统')

        break
    else:
        print("输入错误,请重新选择")
