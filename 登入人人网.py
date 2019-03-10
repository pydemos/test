#! /usr/bin/env python
# coding=utf-8
import requests

# response = requests.get('http://www.baidu.com/')
# print(response.cookies.get_dict())
url = 'http://www.renren.com/PLogin.do'
data = {
        'email': "13045929129",
        'password': 'tai+1992'
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36',
}
session = requests.Session()
session.post(url, data=data, headers=headers)
response = session.get('http://wmw.renren.com/880151247/profile')
with open('renren.html', 'w', encoding='utf-8')as fp:
    fp.write(response.text)
