import requests
from bs4 import BeautifulSoup
import time

url = "https://umei.cc/bizhitupian/weimeibizhi/"
#headers = {
 #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#}
resp = requests.get(url)
resp.encoding ="utf-8"  # 指定字符集
# print(resp.text)

# 将代码交给bs

main_page = BeautifulSoup(resp.text,"html.parser")  # html.parser:处理HTML中的乱码问题
alist = main_page.find("div",class_="TypeList").find_all("a")   # 缩小搜索的范围
# print(alist)
for a in alist:
    href = a.get('href') # 直接通过get来拿到所有的属性的值
    print(href)