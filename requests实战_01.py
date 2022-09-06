import requests

url = 'https://fanyi.baidu.com/sug'

s = input("请输入你想翻译的单词")

dat = {
    "kw":s
}
#发送的post请求，(通过post请求，发送的数据必须放在字典的当中 ，通过data来进行传递)*get和post两种的不同用法*
repson = requests.post(url,data=dat)

print(repson.json()) #将服务器返回的数据转换为json文件，（相当于Python里的字典dic()）
repson.close() #关闭repson