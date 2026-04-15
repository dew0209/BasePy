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

    def done_func(future):
        print('完成完成了：',future.result());

    futures = [p.submit(work,i) for i in range(1,10)]
    for future in futures:
        # 使用add_done_callback方法，为任务添加完成时的回调函数
        future.add_done_callback(done_func)
    p.shutdown(wait=True)
    print('end')
