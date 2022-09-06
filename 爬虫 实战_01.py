import requests

MZ = input("请输入明星的名字")
url = f'https://www.sogou.com/web?query=MZ{MZ}'

dic= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
} #构建虚拟的请求头的参数

resp = requests.get(url,headers=dic)#通过请求头来访问，处理小小的反爬虫。
print(resp)
print(resp.text)#拿到网页页面的源代码