# reduce函数：将一组数据不断”合并“，最终形成一个结果
# 语法：reduce(合并函数,可迭代对象,初始值)
# reduce函数需要从functools模块中引入才能使用
from functools import reduce
nums = [1,2,3,4,5]

def count(a,b):
    # print("count函数调用了：",a,b)
    return a + b
# nums = [1] 单个不调用，直接返回
res = reduce(count,nums)
# res = reduce(count,nums,1) 最后一个是初始值
# 输出结果：15
print(res)

res = reduce(lambda x,y : x + y,nums)
# 输出结果：15
print(res)

# 字符串拼接
nums = ['ab','cd','ef']
res = reduce(lambda x,y : x + y,nums)
# 输出结果：abcdef
print(res)
