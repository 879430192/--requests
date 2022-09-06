#1、拿到contId
#2、拿到videoStatus返回的json, --->  srcURL
#3、srcURL里面的内容进行修整
#4、下载视频

import requests

url = "https://www.pearvideo.com/video_1742466"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.2852240885210744"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Referer": url  #防盗链 ：溯源，当前本次请求的上级是谁
}
resp = requests.get(videoStatusUrl,headers=headers)
#print(resp.text)

dic = resp.json()  #写入字典当中

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}") #将完整的视频的地址进行拼接
#print(srcUrl)

#下载视频
with open("novel/a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
print(f"视频已下载成功")