import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id,RLock

#
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}........{get_native_id()}')
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     print('开始')
#     lock = RLock()
#     p = ThreadPoolExecutor(max_workers=2)
#     # submit：只负责提交任务，不会阻塞主进程
#     p.submit(work,10,lock)
#     p.submit(work,10,lock)
#     p.submit(work,10,lock)
#     # shutdown:不再接受新的任务
#     # wait=True：阻塞线程，等待线程池中所有的任务执行完毕
#     p.shutdown(wait=True)
#     print('结束')
#




def work(n,lock):
    with lock:
        print(f'work正在执行任务{n}........{get_native_id()}')
    if n <= 2:
        time.sleep(3)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

#
# if __name__ == '__main__':
#     print('开始')
#     lock = RLock()
#     p = ThreadPoolExecutor(max_workers=2)
#     futures = [p.submit(work,index,lock) for index in range(10)]
#     p.shutdown(wait=True)
#     # for future in as_completed(futures):
#     #     print(future.result())
#     for future in futures:
#         print(future.result())
#     print('结束')

#
# if __name__ == '__main__':
#     print('开始')
#     lock = RLock()
#     p = ThreadPoolExecutor(max_workers=2)
#     def done(f):
#         print(f.result())
#     for index in range(10):
#         r = p.submit(work, index, lock)
#         r.add_done_callback(done)
#     p.shutdown(wait=True)
#     print('结束')


if __name__ == '__main__':
    print('开始')
    lock = RLock()
    with ThreadPoolExecutor(max_workers=2) as p:
        result = p.map(work,range(10),[lock] * 7)
        print(list(result))
    print('结束')
    