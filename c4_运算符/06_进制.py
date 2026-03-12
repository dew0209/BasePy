# 进制
# 二进制0bxxx或者0Bxxx
num1 = 0b1110
num2 = 0B1110
# 输出结果：14
print(num1)
# 输出结果：14
print(num2)

# 八进制0oxxx或者0O
num3 = 0o321
num4 = 0O321
# 输出结果：209
print(num3)
# 输出结果：209
print(num4)

# 十六进制0x或者0X
num_1 = 0x1A
# 输出结果：26
print(num_1)

# 10进制转2进制字符串 bin(xx)
num5 = bin(8)
# 输出结果：0b1000
print(num5)
# 输出结果：<class 'str'>
print(type(num5))
# 10进制转8进制字符串 oct(xx)
# 10进制转16进制字符串 hex(xx)

# int(a,b)：将指定b进制的字符串a转换为10进制
# 输出结果：7
print(int('0b111',2))