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
    p = ProcessPoolExecutor(max_workers=8)

    futures = [p.submit(work,i) for i in range(1,10)]
    # as_completed:按照完成顺序获取结果
    for fu in as_completed(futures):
        print(fu.result())
    p.shutdown(wait=True)
