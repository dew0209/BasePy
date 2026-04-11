import os
import time
from multiprocessing import Process

def speak():
    for index in range(10):
        print(f'我在说话{index},进程pid是:{os.getpid()}，我的父进程是：{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(15):
        print(f'我在学习{index},进程pid是:{os.getpid()}，我的父进程是：{os.getppid()}')
        time.sleep(1)

# 创建两个 Process 类的实例对象（进程对象
"""
注意点1：p1和p2就对应着以后的两个子进程，在创建他们的时候，就要指定好他们要执行的任务
注意点2：此时的p1和p2只是代码层面的两个进程对象，操作系统还没有真的创建p1和p2两个进程

一定要写 if __name__ == '__main__': 这个判断，原因如下：
1.当创建子进程时，python并不会把父进程内存里的speak函数直接交给子进程
2.python会启动一个全新的python解释器进程，重新执行当前的.py文件（作为模块）
3.在执行过程中，重新定义出一个speak函数，交给子进程

"""
# 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度
# 为什么需要if，防止递归，因为新进程需要找到这个文件 p1 和 p2又创建了一下
if __name__ == '__main__':
    print(os.getpid())
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p2.start()