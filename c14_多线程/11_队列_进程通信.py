import time
from multiprocessing import Queue, Process


def test1(q):
    for i in range(10):
        print(f'test1 放入数据：{i}')
        q.put(i)
        time.sleep(1)


def test2(q):
    for i in range(10):
        print(f'test1 取出数据：{q.get()}')
        time.sleep(0.5)

if __name__ == '__main__':
    q = Queue()
    Process(target=test1,args=(q,)).start()
    Process(target=test2,args=(q,)).start()