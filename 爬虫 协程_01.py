import asyncio
import time

"""
async def func1():
    print("你好我是潘金莲")
   # time.sleep(3)  #当程序出现了同步操作的时候，异步就会被中断
    await asyncio.sleep(3)  #使用异步操作的代码
    print("你好我是潘金莲")

async def func2():
    print("你好我是武大郎")
    await asyncio.sleep(2)  #使用异步操作的代码
    print("你好我是武大郎")

async def func3():
    print("你好我是哈哈哈")
    await asyncio.sleep(4)  #使用异步操作的代码
    print("你好我是哈哈哈")

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    task = [
        f1,f2,f3
    ]
    t1 = time.time()
    asyncio.run(asyncio.wait(task))  #一次性启动多个任务（协程）
    t2 = time.time()
    print(t2-t1)
"""