# 转成字符串
a = str(12)
# 输出结果：<class 'str'>
print(type(a))

# 输出结果：15
print(int(15.6))
# 输出结果：15
print(int('15'))
# 输出结果：15
print(int('  15   '))
# 报错
# print(int('15.6'))

# 输出结果：18.0
print(float(18))
# 输出结果：15.6
print(float('15.6'))
# 输出结果：15.6
print(float('  15.6   '))