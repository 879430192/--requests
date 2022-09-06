# 将程序直接连接到浏览器，让浏览器来完成各种复杂的操作，接收最终的结果
#
# selenium：自动化操作工具
#     打开浏览器来像人一样过来完后才能各种操作。
#     直接提取到网页上的各种信息

# pip install selenium


#让selenium来启动浏览器
from selenium.webdriver import Chrome
#创建浏览器对象
web = Chrome()
# 打开一个网站
web.get("https://www.baidu.com/")

print(web.title)   #打印出网站的标题title

