#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Cat():
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def eat(self):
        print('吃东西')
    def run(self):
        print('跑步')
        #创建猫对象
tom = Cat('xiaoyu',23)
print(tom)

tom.eat()
tom.run()
'''
在程序开发中，要设计一个类，通常需要满足以下三个要素：
1 类名 这类事物的名字，满足大驼峰命名法
2 属性 这类事物具有什么样的特征
3 方法 这类事物具有什么样的行为
大驼峰命名法
1每个单词的首字母大写
2 单词和单词之间没有下划线
3,1 类名的确定
名词提炼法，分析整业务流程，出现的名词，通常就是找到的类个
3.2属性和方法的确定
对象的特征描述，通常可以定义成属性
对象具有的行为，通常可以定义成方法
提示：需求中没有涉及的属性或者方法在设计类时候，不在需要考虑
'''
