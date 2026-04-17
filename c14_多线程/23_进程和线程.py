""""""
import time

"""
cpu密集型任务：
    大部分时间花在算上
    图像处理，视频编码，数值计算，模型训练...
    多进程
I/O密集型任务：
    大部分时间花在等上
    文件I/0，网络请求，操作数据库...
    多线程
"""
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def calc():
    sum = 0
    for i in range(1,10000000):
        sum += i
    return sum

if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as p:
        p.map(calc,range(1,5))
    end = time.time()
    print(f'多花费时间：{end-start}秒')