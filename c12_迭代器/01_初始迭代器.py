# 1.能被for循环遍历的对象，被称为：可迭代对象（iterable）
# region
# names = ['张三','李四','王五']
# msg = 'hello'
# for name in names:
#     print(name)
# for m in msg:
#     print(m)
# endregion

# 2.可迭代对象（iterable）能调用__iter__方法
# 3.调用__iter__会得到一个迭代器（iterator）
#    备注1：__iter__是一个魔法方法，当调用 iter 函数时，__iter__会自动调用
#    备注2：如果iter(obj)能得到一个迭代器（iterator），那obj就是可迭代对象
# region:
# names = ['张三','李四','王五']
# print(names.__iter__())
# for name in names.__iter__():
#     print(name)
# for name in iter(names):
#     print(name)

# True
# print(hasattr(names,'__iter__'))
# endregion

# 4.迭代器拥有__next__方法，每次调用都会根据当前的状态，返回下一个元素
# 备注1：等同于next()
# 备注2：当所有怨怒全都取出后，若继续调用__next__方法，py会抛出 StopIteration 异常
"""
for循环底层就是这样 for item in 可迭代对象,会自动调用iter()
相当于
it = iter(可迭代对象)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration
        break
"""
# region
# names = ['张三','李四','王五']
# it = iter(names)
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(it.__next__())
# endregion

# 5.迭代器也拥有 __iter__方法,并且其返回值是迭代器自身
# 为什么这么设计:让for循环也能遍历迭代器(即:为了让iter(迭代器)不出错)
# region
# names = ['张三','李四','王五']
# it = iter(names)
# 两次打印相同
# print(it)
# print(iter(it))
# endregion

# 6.迭代器协议
# 备注1.能被iter()接受 (__iter__)
# 备注2.next()一步一步取值 (__next__)