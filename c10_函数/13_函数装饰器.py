# 函数装饰器
# 关键点：
# 1.接受被装饰的函数，同时返回新函数
# 2.装饰器吐出来的是wrapper函数，以后别人调用的也是wrapper函数
# 3.为了保证参数的兼容性，wrapper函数要通过 *args 和 **kwargs 接受参数
# 4.wrapper函数中主要做的是：调用原函数，执行其他逻辑，但要记得将原函数的返回值 return 出去
#
# def say_hello(func):
#
#     def wrapper(*args,**kwargs):
#         print('你好，我要开始计算了')
#         res = func(*args,**kwargs)
#         print(f'结算结果：{res}')
#         return res
#     return wrapper
#
#
# def add(a,b):
#     return a+b

# res = add(1,2)
# print(res)

# 在不修改add的前提下，给add函数增强下
# 实现方案：使用装饰器
# say_hello是手动装饰，写起来会麻烦一些，不推荐。推荐：@装饰器
# add_pro = say_hello(add)
#
# res = add_pro(3,4)
#
# print(res)


# 相当于add1 = say_hello(add1)
# @say_hello()
# def add1(a,b):
#     return a+b
#
# @say_hello
# def sub(a,b):
#     return a-b
# add1(1,2)
# sub(1,2)


# 进阶：带参数的装饰器（外层接受配置，中间层接受函数，内层接受具体参数）
# def proxy(msg):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             print(f'你好，我要开始{msg}计算了')
#             return func(*args,**kwargs)
#         return wrapper
#     return outer
#
# # 带参数，拿的是proxy的返回值，给mul增强，也就是outer
# @proxy('乘法')
# def mul(a,b):
#     return a*b
# # 输出结果:
# # 你好，我要开始乘法计算了
# # 6
# print(mul(2,3))


def proxy1(fun):
    print('我是proxy1装饰器')
    def wrapper(*args,**kwargs):
        print('proxy1追加的逻辑')
        return fun(*args,**kwargs)
    return wrapper


def proxy2(fun):
    print('我是proxy2装饰器')
    def wrapper(*args,**kwargs):
        print('proxy2追加的逻辑')
        return fun(*args,**kwargs)
    return wrapper


# proxy2对add增强，形成一个新函数
# proxy1对新函数增强，再生成一个新函数
@proxy1
@proxy2
def add(x,y):
    res = x + y
    print(f'{x} 和 {y} 相加的结果是 {res}')
    return res

# 输出结果：
# 我是proxy2装饰器
# 我是proxy1装饰器
# proxy1追加的逻辑
# proxy2追加的逻辑
# 10 和 20 相加的结果是 30
add(10,20)