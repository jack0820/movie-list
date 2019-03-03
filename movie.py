import requests
import json
from lxml import etree
def gethtml(page):
    page1 = 10*page
    url = "https://maoyan.com/board/4?offset=%d" % page1
    r = requests.get(url)
    return r.text
    #初始化标准化
def gettitles(text):
    html = etree.HTML(a)
    #提取有效信息，利用xpath语法
    #写正则
    #捕捉标题
    titles = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    #捕捉上映时间
    releasetimes = html.xpath('//p[@class="releasetime"]/text()')
    #zip是拉链函数
    item = {}
    for name,realeasetime in zip(titles,releasetimes):
        item['电影名称'] = name
        item[' '] = realeasetime
        yield item 

#保存数据
def save2file(data):
    with open('movie.json','a',encoding='utf-8') as f:
        #json把字典等转变成字符串,false保证中文可读，\n换行
        data = json.dumps(data,ensure_ascii=False) + ',\n'
        f.write(data)
for i in range(1,10):
    a = gethtml(i)
    items = gettitles(a)
    for item in items:
        print(item)
        save2file(item)
