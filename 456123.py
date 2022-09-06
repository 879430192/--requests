import requests

from lxml import etree


url = 'https://www.zhulang.com/search/index.html'

headers = {
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

result = requests.get(url,headers=headers)

# print(resp.text)
html = etree.HTML(result.content)

items = html.xpath('//*[@id="sch-result"]/div[2]/ul/li[1]/dl/dd/h3/a[1]/text()')
print(items)
