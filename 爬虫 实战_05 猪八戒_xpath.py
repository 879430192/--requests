# 拿到猪八戒网页的源代码
# 提取和解析拿到的数据

import requests
from lxml import etree

#确定网站的URL
url = 'https://zhengzhou.zbj.com/search/f/?kw=saas'
resp = requests.get(url)#使用requests的get方法来获取网页的源代码
#print(resp.text)

#解析数据
html = etree.HTML(resp.text)

# 拿到每个商家的价格
price = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div/div/div/a[2]/div[2]/div[1]/span[1]/text()")
for p in price:
    # 每个商家的名称
    company_name = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div/div/div/a[1]/div[1]/p/text()')
    for comname in company_name:
        print(p,comname)
