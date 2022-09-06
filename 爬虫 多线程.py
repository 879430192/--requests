from threading import Thread


class Mythread(Thread):
    def run(self):   #固定的，当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("子线程",i)

if __name__ == '__main__':
    t = Mythread()
    t.start() #开启线程，说明线程的状态

    for i in range(1000):
        print("主线程",i)