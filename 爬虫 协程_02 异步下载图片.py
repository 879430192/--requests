import asyncio
import aiohttp


urls = [
    "https://w.wallhaven.cc/full/72/wallhaven-72e2my.jpg",
    "https://w.wallhaven.cc/full/x8/wallhaven-x8d8pv.jpg",
    "https://w.wallhaven.cc/full/k7/wallhaven-k7lxyd.jpg"
]

async def aiodownload(url):
    #1、发送请求
    #2、得到图片的内容
    #3、保存到文件
    name = url.rsplit("/",1)[1]  #从右边开始切割，取右边的第一个。
    async with aiohttp.ClientSession() as session:   #相当于requests
        async with session.get(url) as resp:        #resp = requests.get()
            #得到请求后写入文件
            with open(name,mode="wb") as f:  # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的。需要使用await进行挂起

    print(name ," 下载完成")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())