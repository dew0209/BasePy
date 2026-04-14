import os
import time
from concurrent.futures import ProcessPoolExecutor

def work(n):
    print(f'work正在执行任务{n}........{os.getpid()}')
    time.sleep(3)


if __name__ == '__main__':
    print('开始')
    p = ProcessPoolExecutor(max_workers=2)
    # submit：只负责提交任务，不会阻塞主进程
    p.submit(work,10)
    p.submit(work,10)
    p.submit(work,10)
    # shutdown:不再接受新的任务
    # wait=True：阻塞进程，等待进程池中所有的任务执行完毕
    p.shutdown(wait=True)
    print('结束')
