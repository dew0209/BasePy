import time
from multiprocessing import Process,Pipe


def test1(con1):
    time.sleep(1)
    con1.send(100)
    print('test1发送了100')


def test2(con2):
    print(f'test2接受了{con2.recv()}')
if __name__ == '__main__':
    # con1,con2 = Pipe(duplex=False),con1只能接受，con2只能发送
    con1,con2 = Pipe()
    Process(target=test1,args=(con1,)).start()
    Process(target=test2,args=(con2,)).start()