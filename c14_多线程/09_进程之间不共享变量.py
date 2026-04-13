""""""

"""
进程之间不共享内存，因此也就不共享任何变量，lock是共享的
"""

num = 100


from multiprocessing import Process


def test1(names):
    global num
    num += 10
    names.append('李四')
    print(f'我是 test1 进程,操作之后的num:{num}，names:{names}')

def test2(names):
    global num
    num -= 10
    names.append('张三')
    print(f'我是 test2 进程,操作之后的num:{num}，names:{names}')

if __name__ == '__main__':
    print('我是主进程中的[第一行]代码')
    names = []
    p1 = Process(target=test1,args=(names,))
    p2 = Process(target=test2,args=(names,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # names打印的还是为空
    print(f'主进程的num:{num},names:{names}')
    print('我是主进程中的[最后一行]代码')