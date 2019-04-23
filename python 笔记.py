#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#元组的定义
#元组与
# python 内置函数
'''
item = "str"
len(item)  # 计算容器中元素的个数
del (item)  # 删除变量
max(item)  # 返回容器中最大值.如果是字典只针对key比较
min(item)  # 返回容器中最小值,如果是字典只针对key比较
# cmp (item1,item2)比较两个值.python3取消了这个函数
# 字符串比较符合一下规则 :"0"<"A"<"a"
# 切片使用索引来限定范围,从一个大的字符串中切出小的字符串
# 列表和元组都是有序的几盒,都能够通过索引值 获取到对应的数据
# 字典是一个无序的几盒,是使用键值对保存数据的,无法进行索引操作
#  "*" 描述:合并. 支持的数据类型:字符串,列表,元组
#  "+" 描述:重复, 支持的数据类型:字符串列表,元组
# in  3 in (1,2,3) True 元素是否存在.支持的数据类型:字符串列表,元组

自定义函数
<1>无参数、无返回值
def函数名（）：
    语句
<2>无参数、有返回值
def函数名（）：
    语句
    return需要返回的数值
注意：
·一个函数到底有没有返回值，就看有没有return，因为只有return才可以返回数据
·在开发中往往根据需求来设计函数需不需要返回值
·函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成
<3>有参数、无返回值
def函数名（形参列表）：
    语句
'''
# 类:是实实在在的对象,看得见摸得着的.先有类才有对象.一个模板.一张图纸
'''
类由3个部分构成
类的名称:类名  (人)
类的属性:一组数据(身高,年龄)
类的方法:允许对进行操作的方法(行为)(跑,打架 )
'''
'''
面向对象
面向过程编程
面向对象编程
类:一个模板
往往用来生成对象-
对象:就是一个个实体,一个猫,一条狗
往往用来.执行实际的功能
抽象:
定义一个类
class 类名:
#属性  类似函数中的变量用来描述对象的特性
#方法  对象拥有的功能，类似函数
class dongwu :
    def __init__(self):
        构造方法
        往往用来设定下一模式的数据
    def __del__(self):
        析构方法
        往往用来,完成数据的清理.或者特定功能的操作
    def diaoxue(self):
        if self.__shengmingzhi>0:
            self.__shengmingzhi -= 10 
    def chi(self):
        print('猫在吃鱼')
    def he（self):
        print('猫在喝')
      def la(self):
        pass
    def sa（self):
        pass
class Cat(dongwu) :
   def play(self):
    pass
class Dog(dongwu):
    def chi(self):
        pass #重写
        dongwu.chi(self)#在子类当中调用在父类当中重写的方法
⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆
class Cat：
    def chi(self):
        print('猫在吃鱼')
    def he（self):
        print('猫在喝')
      def la(self):
        pass
    def sa（self):
        pass
class Dog：
    def chi(self):
        print('狗在吃鱼')
    def he（self):
        print('狗在喝')
      def la(self):
        pass
    def sa（self):
        pass

面向过程开发
变量好比一个容器,购物车
变量名= 值
name = 'zhangsan'
num =100
num2 = num
常量:不能修改的值,就是常量
 100 =3.12
if:判断
if age >=18:
	print('aaaa')
	满足条件True
	不满足条件False
if age >=18 or 20 or 30:
	print('aaa')
通常用True和False来表示满足或者不满足，还有一种情况，也可以表示满足或者不满足
1.只要不是0或者负数，，就表示True
2.只要是0，，，，，就表示False

#aaa
if 嵌套
	if 条件1:
		if 条件2:
#if 外面的条件满足.里面的才能执行的
while :能完成循环的目的
i = 0
while  i< 5:
    print('dsdad')
while True:
    print('yy')
    小技巧:如果不知道明确代码到底执行多少次那么此时就是死循环.否则就采用普通有确定次数的那种循环.
    字符串:'acb',"aacc"
    mystr = 'ffsfsa'
    mystr[0]--->'f'
    mystr[-1]--->'c'
    mystr[3:10]---从下标为3的开始取.一直取到下标为9的那个
    mystr[2:]--->从下标为3的开始取到最后一个
    列表
    name = []
    name.append('zhangsan')
    name.append('lisi')
    names = ['shangsan','lisi']
    如果在定义变量的时候.同时赋予了一个值.那个值叫做初始化
    元组
    names = ('zhangsan','lisi')
    字典
    dict  = {键:值}  dict = {'name':'张撒娇','age':33}
    for :循环
    for i in 字符串.列表.元组.字典.
    num  = '10'
    for i in num:
        print(i) ----> '1'   '0'  '0'
    函数:
        库函数:print(),raw_input()系统给的库函数
        用户自定义函数:开发者自己写的
        如果系统中没有,我们需要的函数,开发者需要自己写,即自定义函数
        def 函数名():
            函数体--->执行的语句
        def test(a,b):
            print('a+b=%d %(a+b)'
            return 100
            return 200
            return 200
            return(100,200,300)
            函数的嵌套调用:
            def a():
                xxx
            def b():
                xxx2
            def c():
                a()
                b ()
     '''
