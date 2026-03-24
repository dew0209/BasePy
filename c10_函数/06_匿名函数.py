# fun = lambda a,b,c:a + b + c
# 输出结果：6
# print(fun(1,2,3))

def calc(fun,a,b):
    print(f'计算结果：{fun(a,b)}')

# 输出结果：
# 计算结果：3
# 计算结果：-1
calc(lambda a,b:a+b,1,2)
calc(lambda a,b:a-b,1,2)