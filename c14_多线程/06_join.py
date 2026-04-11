import time
from multiprocessing import Process

def speak():
    for index in range(10):
        print('好好')
        print('学习')
        print('天天')
        print('向上')
        time.sleep(1)

def study():
    for index in range(15):
        print('day day', end='')
        print('up')
        time.sleep(1)

"""
join方法的作用：阻塞当前进程，等join前面的进程执行完，再继续往下执行
join(timeout)，其中timeout是可选参数，表示等多久，单位是秒

注意点：
    1.p.join() 不是让进程p等，而是让执行这行join代码的那个进程去等，等的是p这个进程
    2.当达到了timeout所指定的时间后，进程并不会终止，只是不再等了
    3.join必须在start之后
"""
if __name__ == '__main__':
    print('---主进程开始---')
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p2.start()
    # 让主进程等待p1执行完毕
    p1.join()
    # 让主进程等待p2执行完毕
    p2.join()
    print('---主进程结束---')
