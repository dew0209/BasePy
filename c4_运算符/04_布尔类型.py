a = True
# 输出结果：True
print(a)
# 输出结果：<class 'bool'>
print(type(a))

# 输出结果：1
print(int(True))
# 输出结果：2
print(1 + True)

# 使用bool()将指定内容转为布尔类型，除0 ''以外都是True
# 输出结果：True
print(bool(1))
# 输出结果：False
print(bool(0))
# 输出结果：True
print(bool('2'))
# 输出结果：False
print(bool(''))