import os
import time
from concurrent.futures import ProcessPoolExecutor,as_completed


def work(n):
    print(f'work正在执行任务{n}........{os.getpid()}')

    if n < 3:
        time.sleep(6)
    else:
        time.sleep(1)

    return f'我是任务{n}的结果'


if __name__ == '__main__':
    print('开始')
    # with:自动shutdown
    with ProcessPoolExecutor(max_workers=8) as p:
        res = p.map(work,range(1,10))
        for r in res:
            print(r)
        print('end')
