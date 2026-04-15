import os
import time
from threading import get_native_id,Thread,RLock


def speak(lock):
    for index in range(10):
        with lock:
            print(f'我在说话{index},进程pid是:{os.getpid()}，线程编号：{get_native_id()}')
        time.sleep(1)

def study(lock):
    for index in range(15):
        with lock:
            print(f'我在学习{index},进程pid是:{os.getpid()}，线程编号：{get_native_id()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'---start---,进程pid是:{os.getpid()}，线程编号：{get_native_id()}')
    lock = RLock()
    """
    Thread 参数：
        1.group：默认值为None（应当始终为None）
        2.target：线程要执行的可调用对象，默认值为None
        3.name：线程名称，默认为None，如果设置为None，Python会自动分配名字
        4.args：给target传的位置参数（元组）
        5.kwargs：给target传的关键字参数（字典）
        6.daemon：标记线程是否为守护进程，取值为布尔值（默认为None）
    """
    t1 = Thread(target=speak,args=(lock,))
    t2 = Thread(target=study,args=(lock,))
    t1.start()
    t2.start()
    # 让主进程等 t1 和 t2 线程执行完毕后，主线程再继续执行
    t1.join()
    t2.join()
    print(f'---end---,进程pid是:{os.getpid()}，线程编号：{get_native_id()}')
