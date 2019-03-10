#! /usr/bin/env python
# coding=utf-8
# ! /usr/bin/env python
# coding=utf-8
# 大鹏个人主页     http://wmw.renren.com/880151247/profile
# 人人网登入主页  http://www.renren.com/SysHome.do
from urllib import request
from  urllib import parse
from  http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'
}


def get_openr():
    # 1登录
    # 1.1创建一个cookidejar对象
    cookidejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcessor对象
    handeler = request.HTTPCookieProcessor(cookidejar)
    # 1.3 使用上一个步骤创建的handeler 创建一个opener
    opener = request.build_opener(handeler)
    return opener


def login_renren(opener):
    # 1.4 使用opener 发送登录的请求(人人网的邮箱和密码)
    data = {
        'email': "13045929129",
        'password': 'tai+1992'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(
data).encode('utf-8'), headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2访问个人主页
    dapeng_url = 'http://wmw.renren.com/880151247/profile'
    # 获取个人主页的页面的时候.不更新建一个opener,而应该使用之前的一个opener
    # 已经包含了之前登录的cookie的信息
    req = request.Request(dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as  fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ - - '__main__':
    opener = get_openr()
    login_renren(opener)
    visit_profile(opener)
