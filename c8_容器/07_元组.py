t1= (27,28,33)

# 输出结果：<class 'tuple'>
print(type(t1))
# 输出结果：27
print(t1[0])
# 输出结果：33
print(t1[-1])

t2 = ()
t3 = tuple()
t4 = ('您好',)
# 输出结果：<class 'tuple'>
print(type(t2))
# 输出结果：<class 'tuple'>
print(type(t3))
# 输出结果：<class 'tuple'>
print(type(t4))


t4 = (12,33,12,33,45)
# 输出结果：1
print(t4.index(33))
# 输出结果：2
print(t4.count(33))

t5 = sorted(t4)
# 输出结果：<class 'list'>
print(type(t5))
# 输出结果：[12, 12, 33, 33, 45]
print(t5)
t6 = tuple(t5)
# 输出结果：<class 'tuple'>
print(type(t6))
# 输出结果：(12, 12, 33, 33, 45)
print(t6)

def demo(*args):
    print(type(args))
# 输出结果：<class 'tuple'>
demo(1,2,3)


def demo1(**args):
    # 输出结果：<class 'dict'>
    print(type(args))
# 输出结果：<class 'tuple'>
demo1(a = 1,b = 2,c = 3)
