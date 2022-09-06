# 1、如何提取单个页面的数据
# 2、通过线程池来进行多个页面的同时抓取。

import requests
from lxml import etree
import csv

f = open("novel/caijia.csv", mode="w", encoding="utf-8")
csvWrite = csv.writer(f)


def download_one_page(url):
    # 拿取页面的源代码
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    resp = requests.get(url,headers=headers)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol")[0]
    print(table)
    #trs = table.xpath("./tr")[1:]
    #拿到每一个tr
    #for tr in trs:
        #txt = tr.xpath("./td/text()")
        #对数据进行简单的处理



if __name__ == '__main__':
    download_one_page = ("https://movie.douban.com/top250?start=50&filter=")