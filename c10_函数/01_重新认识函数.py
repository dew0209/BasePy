# 1.函数也是对象
def welcome():
    print('您好')
# 输出结果：<class 'function'>
print(type(welcome))

# 2.函数可以动态添加属性
welcome.desc = '这是一个打招呼的函数'
# 输出结果：这是一个打招呼的函数
print(welcome.desc)

# 3.函数可以赋值给变量
a = welcome
# 输出结果：您好
a()

# 4.可变参数 vs 不可变参数
# 不可变参数：无论怎么改，外侧的a不变
a = 666
def welcome1(data):
    print(f'data修改前{data}，{id(data)}')
    data = 999
    print(f'data修改后{data}，{id(data)}')
print('调用函数前',a,id(a))
welcome1(a)
print('调用函数后',a,id(a))

# 不可变参数：能改变外侧的a
a = [10,20,30]
def welcome2(data):
    print(f'data修改前{data}，{id(data)}')
    data[0] = 40
    print(f'data修改后{data}，{id(data)}')
print('调用函数前',a,id(a))
welcome2(a)
print('调用函数后',a,id(a))

# 5.函数也可以作为参数

def welcome3():
    print('您好啊')
def caller(f):
    print('caller调用了')
    f()
# 输出结果：
"""
caller调用了
您好啊
"""
caller(welcome3)
# 6.函数也可以作为返回值

def welcome4():
    print('你好啊')
    def show_msg(msg):
        print(msg)
    return show_msg
# 输出结果：
"""
你好啊
测试函数作为返回值
"""
fun = welcome4()
fun('测试函数作为返回值')