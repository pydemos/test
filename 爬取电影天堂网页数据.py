#! /usr/bin/env python
# coding=utf-8
from  lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
# url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/63.0.3239.132 Safari/537.36"
}


def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    # print(response.text)
    # response.text
    # response.content
    # requests库.默认会使自己猜测的编码方式将
    # 抓取下来的网页进行解码.然后存储到text的属性上去
    # 在电影天堂的网页中,因为编方式.request库猜错了.所以就产生乱码
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    pass


def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
    for x in range(1, 8):
        url = base_url.format(x)
        movie = parse_detail_page(url)

if __name__ == '__main__':
    spider()
