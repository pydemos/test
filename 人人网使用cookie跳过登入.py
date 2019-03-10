#! /usr/bin/env python
# coding=utf-8
# 大鹏个人主页     http://wmw.renren.com/880151247/profile
# 人人网登入主页  http://www.renren.com/SysHome.do
from urllib import request
from urllib import parse

dapeng_url = 'http://wmw.renren.com/880151247/profile'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'anonymid=jreu3w32x0acc4; depovince=FJ; _r01_=1; ick_login=f6b18a48-6568-4fc1-b920-ce67756d8aae; ick=0d594766-1141-4454-ab3b-3037902a7663; __utma=151146938.1479862020.1548590365.1548590365.1548590365.1; __utmc=151146938; __utmz=151146938.1548590365.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do; __utmt=1; _de=85E3DAAB35E57880F7DC708369CBDF64; __utmb=151146938.7.10.1548590365; jebecookies=5d8fc46b-e9cd-46dd-b1ea-175998e021f2|||||; p=bcc70a4ec92e78f2a0787245fb79f3571; first_login_flag=1; ln_uact=13045929129; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=048405a0e0c5fed07163cad1fdeb270c1; societyguester=048405a0e0c5fed07163cad1fdeb270c1; id=967213501; xnsid=70cfa3a3; ver=7.0; loginfrom=null; jebe_key=6e290c9c-ae75-4ced-970a-7bad565e962e%7Cbba3e9a0ec0e50da5299b3bd4f6ff5f5%7C1548590542474%7C1%7C1548590543756; wp_fold=0'
}
req = request.Request(url=dapeng_url, headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html', 'w', encoding='utf-8') as fp:
    # write的函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes的数据类型
    # bytes-->decode-->str
    # str-->encode-->byes
    fp.write(resp.read().decode('utf-8'))
