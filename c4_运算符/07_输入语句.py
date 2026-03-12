# input()

# 输入18
age = input('请输入你的年龄：')
# 输出结果：<class 'str'>
print(type(age))
# 输出结果：你今年的年龄是18
print(f'你今年的年龄是{age}')
# 输出结果：你今年的年龄是19
print(f'你今年的年龄是{int(age) + 1}')