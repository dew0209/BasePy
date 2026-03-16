def greet(*name,a):
    print(f'{len(name)},{a}')
# 输出结果：3,2
greet(   '1','2','3',a = '2')

def greet1(name,**a):
    print(f'{name},{len(a)}')

# 输出结果：测试,4
greet1('测试',a = '2',b = '1',c = '2',d = '3')

def greet3(*name,**a):
    print(f'{len(name)},{len(a)}')

# 输出结果：3,4
greet3('1','2',3,a = 1,b = 2,c = 3,d = 4)

# 先后保证关键字参数规则：使用关键字参数时，位置参数（如果有）必须在关键字参数之前，把*看成位置参数，把**看成位置参数就行。