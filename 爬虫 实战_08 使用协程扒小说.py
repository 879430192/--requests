
#'URL: http://dushu.baidu.com/a pi/pc/getCatalog?data={"book_id":"4306063500"}'
#章节内部的内容
#http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid"":"4306063500|11348571","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import aiofiles
import json


"""
1、同步操作：访问getCatalog 拿到所有的章节的cid和名称
2、异步操作：访问getChapterContent  将所有的章节内容进行下载
"""

async def aiodownload(cid,b_id,title):
    data = {
        "book_id":b_id,
        "cid":f"{b_id} | {cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open(title,"w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])   #将小说的内容写进文件

async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  #item就是对应的每一个章节的cid
        title = item['title']
        cid = item['cid']
        #准备异步任务
        tasks.append(aiodownload(cid,b_id,title))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    asyncio.run(getCatalog(url))


# 下载的路径文件内容为空