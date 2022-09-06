import time


def func():
    print("我爱黎明")
    time.sleep(3)  #让当前的线程处于阻塞状态，CPU不会开始工作
    print("我真的爱黎明")


if __name__ == '__main__':
    func()



# input（）  程序也会进入阻塞状态
# requests.get(*****)  在网络请求返回数据之前，程序也是进入阻塞的状态。
# 一半情况下，当程序处于IO状态的时候，线程都会处于阻塞状态   IO：input/output

#协程： 当程序遇见IO操作的时候，可以选择性的切换到其他的任务之上

