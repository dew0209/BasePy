# ==
a = 1
b = 1
c = '1'
d = 4
# 输出结果：True
print(a == b)
# 输出结果：False
print(b == c)

# > 左右两侧数据类型一致
e = 9
f = 10
g = 'c'
# 输出结果：False
print(e > f)
# 报错
#print(e > g)

# !=
h = 10
i = 10
j = '10'

# 输出结果：True
print(h != j)
# 输出结果：False
print(h != i)

# 输出结果：49
print(ord('1'))
# 输出结果：我
print(chr(25105))