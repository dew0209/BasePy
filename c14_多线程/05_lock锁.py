import os
import time
from multiprocessing import Process,current_process,Lock,RLock

def speak(lock):
    for index in range(10):
        with lock:
            print('好好')
            print('学习')
            print('天天')
            print('向上')
        time.sleep(1)

def study(lock):
    for index in range(15):
        """
        with lock:会自动完成两件事
            1.进入前：自动执行 lock.acquire() 上锁
            2.离开后：自动执行 lock.release() 释放锁
            好处：即使代码块里发生异常，也能保证释放锁，避免卡死
        Rlock锁：带次数，有几次lock.acquire()就需要lock.release()几次
        """
        with lock:
            print('day day',end='')
            print('up')
        time.sleep(1)

if __name__ == '__main__':
    # lock = Lock()
    lock = RLock()
    p1 = Process(target=speak,args=(lock,))
    p2 = Process(target=study,args=(lock,))
    p1.start()
    p2.start()