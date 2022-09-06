import requests
from lxml import etree

url = "******"

resp = requests.get(url)

html = etree.HTML(resp.text)

result = html.xpath("")

print(result)

#简单的xpath爬取某网站的排行榜信息，