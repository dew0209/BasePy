def greet(name = '张三',gender = '男',gae = 18):
    print(f'{name},{gender},{gae}')

# 输出结果：李四,男,18
greet('李四')
# 输出结果：李四,女,18
greet('李四','女')
# 输出结果：20,男,18
greet(20)
# 输出结果：男,66,18
greet('男',66)

# 从头依次配置
