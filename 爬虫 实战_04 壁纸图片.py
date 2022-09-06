# 1、拿到主页面的源代码，然后提取到子页面的链接地址， href
# 2、通过 href拿到子页面的内容，从子页面之中找到图片的下载地址 img ——> src
# 3、下载图片

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
alist = main_page.find("div", class_="TypeList").find_all("a")   # 缩小搜索的范围
# print(alist)
for a in alist:
    href = a.get('href') # 直接通过get来拿到所有的属性的值
    #print(href)
    # 获取子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到下载的途径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    p = child_page.find("p",align="center")
    img = p.find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)
    img_resp.content  #这里拿到网站的字节
    img_name = src.split("/")[-1]  #拿到URL中的最后一个"/" 以后的内容
    with open("img/"+img_name,mode="wb") as f:
        f.write(img_name.content)  # 将图片内容写入进文件之中

    print("over!!",img_name)
    time.sleep(1)  #休眠时间


print("all over!!!")



#运行结果不正确，href里拿到的网站地址html少了一个l，正则有问题