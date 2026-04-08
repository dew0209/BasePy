""""""
"""
生成器：
    1.生成器函数：函数体中如果出现了yield关键字，那该函数是生成器函数
    2.生成器对象：调用生成器函数时，其函数不会立刻执行，而是返回一个生成器对象


"""

# region
# def demo():
#     print('函数开始执行了')
#     print(100)
#     yield
#     a = 200
#     print(a)
#
# d = demo()
# <generator object demo at 0x0000013D3DD2CEE0>
# print(d)
# endregion

"""
写在生成器函数中的代码，需要通过生成器对象来执行：
    1.调用生成器对象的__next__方法，会让生成器函数中的代码开始执行
    2.当生成器函数中的代码开始执行后，遇到yield会暂停执行，并且其内部会记录暂停的位置
    3.遇到return会抛出 StopIteration 异常，并将return后面的表达式，作为异常信息
    4.yield后面所写的表达式，会作为本次__next__方法的返回值。print(next(d))会为None
"""

# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield
#     a = 200
#     print(a)
#     yield '有返回值'
#     b = 300
#     print(b)
#     return '你好'
#
# d = demo()
# print(next(d))
# print(next(d))
# StopIteration异常
# next(d)

#
# try:
#     next(d)
# except StopIteration as e:
#     print(e)

# endregion


"""
生成器对象是一种特殊的迭代器（本质是通过 yield 自动实现了迭代器协议）

"""
# region

#
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield '有返回值1'
#     a = 200
#     print(a)
#     yield '有返回值2'
#     b = 300
#     print(b)
#     return '你好'
#
# d = demo()
# 验证：生成器对象d，和迭代器一样，也有 __iter__ 和 __next__
# True
# print(hasattr(d,'__next__'))
# print(hasattr(d,'__next__'))

# 验证：生成器对象的 __iter__ 方法，和迭代器一样，返回的也是自身
# True
# result = iter(d)
# print(result == d)

# 为什么没有异常：迭代器本身是靠捕获异常退出循环的
"""
相当于
it = iter(可迭代对象)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration
        break
"""
# for i in d:
#     print(i)

# endregion

"""
yield也能写在循环里
"""
# region
# def create_car(total):
#     for i in range(1,total + 1):
#         yield f'我是第{i}台车'

# d是生成器对象
# d = create_car(10)
# for item in d:
#     print(item)

# endregion

"""
yield from 能把一个可迭代对象里的东西依次yield出去（替代：for + yield）
"""
# region
# def demo():
#     nums = [2,10,3,33,20]
#     yield from nums
#
# d = demo()
# for item in d:
#     print(item)
# endregion

"""
生成器.send(值)，可以让生成器继续执行的同时，给上一次yield传值
    next只能取值，send既能取值，也能送值
"""
# region
# def demo():
#     print('函数开始执行了')
#     print(100)
#     a = yield '我是第一个yield所返回的数据'
#     print(a)
#     b = yield '我是第二个yield所返回的数据'
#     print(b)
#     return '你好'
#
# d = demo()
# 先要next下，让其到yield的位置，可以写成 d.send(None)
# next(d)
# d.send(200)
# d.send(300)
# endregion

"""
生成器实现遍历Person对象
"""
# region
# class Person:
#     def __init__(self,name,age,gender,address):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.address=address
#     def __iter__(self):
#         yield self.name
#         yield self.age
#         yield self.gender
#         yield self.address
#
# p = Person('张三',12,'男','合肥')
#
# for item in p:
#     print(item)

# 无论是迭代器还是生成器对象，都可以使用list,tuple,set等直接拿到其里面的所有内容（多了的话，容易挤爆内存）
# ['张三', 12, '男', '合肥']
# print(list(p))

# endregion


"""
生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象
语法：(表达式 for 变量 in 可迭代对象)
什么时候适合用生成器表达式：当”每个结果，只依赖当前这一个元素时“
"""
# region
nums = [10,20,30,1]

# 列表推导式
result = [it * 2 for it in nums]
# [20, 40, 60, 2]
print(result)
# 生成器推导式
result2 = (it * 2 for it in nums)
# <generator object <genexpr> at 0x000001E6FD0BCEE0>
print(result2)

# endregion