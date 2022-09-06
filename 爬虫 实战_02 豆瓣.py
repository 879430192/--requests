import requests
import re
import csv

url = 'https://movie.douban.com/chart'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

respon = requests.get(url,headers=headers)
page = respon.text
# print(page)

#开始使用正则来进行匹配
ob = re.compile(r' <table width="100%" class="">.*?title="(?P<name>.*?)">',re.S)
result = ob.finditer(page)
f = open("novel/data.csv", mode="w", encoding ="utf-8")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    dic = it.groupdict()
    csvwriter.writerow(dic.values())

f.close()
print(f"结束了")