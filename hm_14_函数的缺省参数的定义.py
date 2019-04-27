#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
def print_info (name,tittle='',gender='男生' ):
    '''

    :param tittle:职位
    :param name: 班上同学的名字
    :param gender: True 男生flase 女生
    :return:
    '''
    gender_text = '男生'
    if not gender :
        gender_text = '女生'
    print('[%s ]%s  是 %s'%(tittle ,name,gender_text))
#假设班上同学,男生居多!
#提示:在指定缺省,参数的默认值.应该使用最常见的值作为默认值!
#如果一个参数的值不能确定,则不应该设置默认值.具体的数值在调用函数时,由外接传递
#缺省函数的定义位置:1 必须保证带有默认值的缺省参数.在参数列表的末尾
#调用多个缺省参数的函数
#1在调用函数是.如果有多个缺省参数,需要指定参数名.这样解释器才能够知道参数的对应关系!
print_info('小明', )
print_info('小妹',False)
