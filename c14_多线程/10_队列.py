""""""
import time

"""
我们之前学过 list tuple dict 它们的特点是：数据想怎么拿数据，就怎么拿

队列（Queue）是：一种“先进先出”的数据结构（先放进去的数据，一定会先取出来）


队列具备等待模式
1.当队列已满，继续put，就会进入等待模式，等别人调用get方法，取走一个元素
2.当队列已满，执行：put(元素,timeout=秒数),就会等待指定秒数
3.put_nowait方法：会直接向队列中添加元素，不会进入等待模式，若队列已满，会抛出异常
    相当于：q2.put(6,block=False)
4.当队列已空，继续 get，就会进入等待模式
5.当队列已空，执行get(timeout=秒数)，就会等待指定秒数
6.get_nowait方法，会直接读取队列中的元素，不会进入等待模式，若队列已空，会抛出异常
    相当于：q2.get(block=False)

"""

from multiprocessing import Queue, Process


# 创建一个队列（不限制大小，即：不设置容量上限）
# q1 = Queue()
# q1.put(1)
# q1.put(2)
#
# print("是否为空：",q1.empty())
# print("结果：",q1.get())
# print("结果：",q1.get())
# print("是否为空：",q1.empty())
# print("是否满了：",q1.full())
# print("获取队列长度：",q1.qsize())
#
#

# 创建一个队列（最多能保存3个元素）
# q2 = Queue(3)
# q2.put(4)
# q2.put(5)
# q2.put(6)
# 不等待直接放入，满了就抛异常
# q2.put(6,block=False)
# 等待
# q2.put(6)
# print('是否满了',q2.full())
# print('大小',q2.qsize())

def test(q):
    time.sleep(3)
    result = q.get()
    print(f'获得元素：{result}')
if __name__ == '__main__':
    q = Queue(2)
    q.put(1)
    q.put(2)
    print(f'队列是否满了：{q.full()}')
    Process(target=test,args=(q,)).start()

    print('向已满的queue添加元素....')
    q.put(3)

    print('目前队列中的元素是：')
    print(q.get())
    print(q.get())
