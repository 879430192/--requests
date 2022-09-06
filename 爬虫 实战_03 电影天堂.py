#要求：
# 1、定位到2020必看片网址
# 2、从2020必看片中提取到子页面的链接地址
# 3、请求页面的链接地址，拿到想要的下载地址。。。。
import requests
import  re
# from typing import List

domain = "https://dytt89.com/"

respon = requests.get(domain,verify=False)  # verify=False :去掉网站的安全认证
respon.encoding = 'gb2312'    # 指定网站的字符集编码格式，

# print(respon.text)


# 拿到 ul 里的 li
ob1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
# 从l li 里面提取子页面的超链接
ob2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
ob3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgc'
                 r'olor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1 = ob1.finditer(respon.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    # 提取到每个子页面的链接
    result2 = ob2.finditer(ul)
    for itt in result2:
        # 拼接完整的网站URL的地址：域名 + 子页面的地址
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)  #将子页面的地址全部保存进列表之中

# 提取每一个子页面的内容
for href in  child_href_list:
    child_respon = requests.get(href,verify=False)
    child_respon.encoding = 'gb2312'
    print(child_respon.text)
    result3 = ob3.search(child_respon.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    #break


