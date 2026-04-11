import os
import time
from multiprocessing import Process,current_process

def speak(a,b,msg):
    for index in range(10):
        print(f'{a}----{b}----{msg}----{current_process().name}---,我在说话{index},进程pid是:{os.getpid()}，我的父进程是：{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(15):
        print(f'我在学习{index},进程pid是:{os.getpid()}，我的父进程是：{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    """
    Process参数：
        1.group：默认值为None（应当始终为None）
        2.target：子进程要执行的可调用对象，默认值为None
        3.name：进程名称，默认为None，如果设置为None，Python会自动分配名字
        4.args：给target传的位置参数（元组）
        5.kwargs：给target传的关键字参数（字典）
        6.daemon：标记进程是否为守护进程，取值为布尔值（默认为None，表示从创建方进程继承）
    """
    p1 = Process(target=speak, args=(1,2),kwargs={'msg':'测试'})
    p2 = Process(target=study)
    p1.start()
    p2.start()