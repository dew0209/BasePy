# 可变集合
s1 = {10,20,30,10,1,True}
# 输出结果：{1, 10, 20, 30}
print(s1)
# 输出结果：<class 'set'>
print(type(s1))

s1.add(3000)
# 输出结果：{1, 10, 20, 3000, 30}
print(s1)

s2 = frozenset({10,20,30,True,1})
# 输出结果：frozenset({True, 10, 20, 30})
print(s2)
# 输出结果：<class 'frozenset'>
print(type(s2))


s3 = frozenset([1,3,4])
# 输出结果：frozenset({1, 3, 4})
print(s3)
# 输出结果：<class 'frozenset'>
print(type(s3))

# 不能嵌套可变集合：报错
# s4 = {20,s1}
# print(s4)

# 可以嵌套不可变集合
s4 = {20,s3}
# 输出结果：{20, frozenset({1, 3, 4})}
print(s4)