#用户将视频进行上传  ——>   转码（将视频处理成2K，1080，标清）  ——>  切片处理（把单个的文件进行拆分）


# 需要一个文件来记录：1、视频的播放顺序     2、视频存放的路径。
# M3U文件  经过utf-8进行编码过后是M3U8文件


#抓取视频的原理：
# 1、找到网站的M3U8文件（各种不同的手段）
# 2、通过M3U8来下载ts文件
# 3、通过各种手段来讲全部的ts文件合并成一个MP4文件


# 爬取的流程：
#     1、拿到网站页面的源代码
#     2、从源代码中提取m3u8的url
#     3、下载m3u8
#     4、读取m3u8文件，下载视频
#     5、合并视频


import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

url = "https://91kanju.com/vod-play/59902-1-1.html"

resp = requests.get(url,verify=False,headers=headers)

print(resp.text)