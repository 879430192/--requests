import requests
from bs4 import BeautifulSoup
import time

url = "https://umei.cc/bizhitupian/weimeibizhi/"
#headers = {
 #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#}
resp = requests.get(url)
resp.encoding ="utf-8"  # 指定字符集#
print(resp.text)
