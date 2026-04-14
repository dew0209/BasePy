import os
import time
from concurrent.futures import ProcessPoolExecutor


def work(n):
    print(f'work正在执行任务{n}........{os.getpid()}')
    time.sleep(3)
    return f'我是任务{n}的结果'


if __name__ == '__main__':
    print('开始')
    p = ProcessPoolExecutor(max_workers=2)
    # submit：只负责提交任务，不会阻塞主进程
    # r1 = p.submit(work,1)
    # r2 = p.submit(work,2)
    # r3 = p.submit(work,3)

    # 不阻塞
    # print(r1)

    # 阻塞，等待执行完成并返回结果
    # print(r1.result())
    # print(r2.result())
    # print(r3.result())
    # print('结束')

    futures = [p.submit(work,i) for i in range(1,10)]

    p.shutdown(wait=True)

    for fu in futures:
        print(fu.result())
