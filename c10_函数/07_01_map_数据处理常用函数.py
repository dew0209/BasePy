# map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据
# 语法：map(函数操作,可迭代对象)

nums = [10,20,30,40]
def double(x):
    return x*2
# map返回的是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
# res = map(double,nums)
res = map(lambda x : x * 2,nums)

# 输出结果：<map object at 0x00000202B4ECBD80>
print(res)
# 输出结果：<class 'map'>
print(type(res))
# 输出结果：[20, 40, 60, 80]
print(list(res))
# 输出结果：[10, 20, 30, 40]。不改变原数据
print(nums)

names = ('python','java','js')
res = map(lambda x : x.upper(),names)
# 输出结果：('PYTHON', 'JAVA', 'JS')
print(tuple(res))
# 输出结果：()  迭代器被耗尽了，你可以搞个变量接收下就行a = tuple(res)
print(tuple(res))

