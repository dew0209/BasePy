# and or not

# and
# 输出True
print(True and False)

# 输出结果2 左边bool(1)为True，看右边bool(2)为True，返回2
print(1 and 2)
# 输出结果0 左边bool(1)为True，看右边bool(0)为False，返回0
print(1 and 0)
# 输出结果0 左边bool(0)为False，不看右边，返回0
print(0 and 1)


# or
# 输出结果：1
print(0 or 1)
#输出结果：空字符串
print(0 or '')

# not
# 输出结果：False
print(not 1)
# 输出结果：True
print(not 0)