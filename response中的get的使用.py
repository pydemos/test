#! /usr/bin/env python
#coding=utf-8
import requests
# response=requests.get('http://www.baidu.com/')
# print(type(response.content))
# print(response.content)
# print(response.content.decode('utf-8'))
# requests
# 发送get请求
# response 的一些属性
# 发送post 请求
# 处理cookie
# 处理没有授权的http协议
params  = {
    'wd':'中国'
}
headers ={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
response =  requests.get('https://www.baidu.com/s',params=params,headers=headers)
with open('baidu.html','w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))
print(response.url)



# requests笔记
# 发送get的请求.直接调用'requests.get'就可以了,想要发送什么类型的请求,就调用什么办法,
# 发送get请求:
'''python
respones = requests.get('https://www.baidu.com')
'''
# response的一些属性:
'''python
import requests

params  = {
    'wd':'中国'
}
headers ={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
#:params
#接收一个字段或者字符串的查询参数,字典的类型自动转换为url编码,不要在urlencode()

response =  requests.get('https://www.baidu.com/s',params=params,headers=headers)
with open('baidu.html','w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))
print(response.url)
#查看响应的内容,response.test返回的是unicode的格式数据
print(response.content)
#查看完成的url地址
print(response.url)
#查看响应头不部的字符编码
print(response.encodeing)
#查看响应码
print(response.status_code)
'''


