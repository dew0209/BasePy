# None

def greet(name,age):
    print(f'{name},{age}')

age = greet('1',22)

# 输出结果：None
print(age)
# 输出结果：<class 'NoneType'>
print(type(age))
# 输出结果：False
print (bool(None))