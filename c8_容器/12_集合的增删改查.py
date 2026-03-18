# 增

s1 = {10,20}
s1.add(30)
# 输出结果：{10, 20, 30}
print(s1)
s1.update([1,2,3])
# 输出结果：{1, 2, 3, 10, 20, 30}
print(s1)

# 删

s2 = {10,20,30,66}
s2.remove(20)
# 输出结果：{10,66,30}
print(s2)
# 报错
# s2.remove(9)
s2.discard(9)
re = s2.pop()
# 输出结果：10
print(re)

# 改 没有下标，改的话只能投机取巧。remove + add 组和
s2.remove(66)
s2.add(90)

# 查
# 输出结果：True
print(30 in s2)
# 输出结果：True
print(99990 not in s2)