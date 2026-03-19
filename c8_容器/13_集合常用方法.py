# difference
s1 = {1,2,3}
s2 = {5,2,3}
# 输出结果：{1}
print(s1.difference(s2))
# 输出结果：{5}
print(s2.difference(s1))

# difference_update
s1.difference_update(s2)
# 输出结果：1
print(s1)

# union
# 输出结果：{1, 2, 3, 5}
print(s1.union(s2))

# issubset
# 输出结果：False
print(s1.issubset(s2))
s2.add(1)
# 输出结果：True
print(s1.issubset(s2))

# issuperset
# 输出结果：True
print(s2.issuperset(s1))

# isdisjoint
# 输出结果：False
print(s1.isdisjoint(s2))