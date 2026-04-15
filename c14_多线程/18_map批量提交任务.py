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
    # 使用map方法批量提交任务（注意：map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
    res = p.map(work,range(1,10))
    # 迭代器
    # <generator object _chain_from_iterable_of_lists at 0x00000230A9E213C0>
    print(res)
    for r in res:
        print(r)
    p.shutdown(wait=True)
    print('end')
