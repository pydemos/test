#! /usr/bin/env python
#coding=utf-8
import  requests
from lxml import  etree
#1将目标网站的页面抓取下来
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/63.0.3239.132 Safari/537.36",
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/xiamen/'
response = requests.get(url,headers=headers)
text =response.text
# requests.text返回的是一个经过解码后的字符串,是str(uncode)类型
#requests.content 返回的是一个原生的字符串,是从网页上抓取下来的,没有经过处理的字符串,字符串类型是bytes类型
#2将抓取下来的数据根据一定的规格进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath('./li')
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")
    thumbanil = li.xpath(".//img")
movie= {
    'title' : title,
    'score' : score,
    'duration' :duration,
    'region' : region,
    'director' : director,
    'actors' : actors,
    'thumbanil' :thumbanil,
}
movies.append(movie)
print(movies[0])