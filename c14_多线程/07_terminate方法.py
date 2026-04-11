import time
from multiprocessing import Process

def speak():
    try:
        for index in range(10):
            print('好好')
            print('学习')
            print('天天')
            print('向上')
            time.sleep(1)
    finally:
        # 使用 terminate 终止进程，不会引起 finally 执行
        print('speak结束')
def study():
    for index in range(15):
        print('day day', end='')
        print('up')
        time.sleep(1)

"""

"""
if __name__ == '__main__':
    print('---主进程开始---')
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p2.start()
    time.sleep(3)
    # 向操作系统申请强制终止p1进程
    p1.terminate()
    # 向操作系统申请强制终止p2进程
    p2.terminate()
    # 等操作系统彻底终止掉了p1
    p1.join()
    # 等操作系统彻底终止掉了p2
    p2.join()
    # 看一下p1是否活者
    print(p1.is_alive())
    print('---主进程结束---')
