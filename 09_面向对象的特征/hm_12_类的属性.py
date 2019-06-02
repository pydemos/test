#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Tool(object):
    count = 0
    def __init__(self,name):
        self.name = name
        #让类属性的值➕1
        Tool.count +=1
#1创建工具对象
tool1 = Tool('斧头')
tool2= Tool('榔头')
tool3= Tool('水桶')
#2输出工具对象的总数
tool3.count = 99
print('工具的对象的总数是%d '%Tool.count)
print('工具的对象的总数是%d '%tool3.count)
'''
访问类属性有两种方式
1.类名.类属性
2.对象.类叔叔(不推荐)
注意:如果使用对象,类属性 = 值 .赋值语句.只会给对象添加一个属性,而不会影响到类属性的值
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class Tool(object):
    count = 0
    def __init__(self,name):
        self.name = name
        #让类属性的值➕1
        Tool.count +=1
#1创建工具对象
tool1 = Tool('斧头')
tool2= Tool('榔头')
tool3= Tool('水桶')
#2输出工具对象的总数
tool3.count = 99
print('工具的对象的总数是%d '%Tool.count)
print('工具的对象的总数是%d '%tool3.count)
'''
访问类属性有两种方式
1.类名.类属性
2.对象.类叔叔(不推荐)
注意:如果使用对象,类属性 = 值 .赋值语句.只会给对象添加一个属性,而不会影响到类属性的值
'''
