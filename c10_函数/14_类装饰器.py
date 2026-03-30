# 类装饰器：
# 1.包含__call__方法的类，就是类装饰器
# 2.像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用
# 3.__call__方法通常接受一个函数作为参数，并且会返回一个新的函数

# class SayHello:
#     def __call__(self,func):
#         def wrapper(*args,**kwargs):
#             print('我要开始计算了')
#             res = func(*args,**kwargs)
#             return res
#         return wrapper
#
# def add(x,y):
#     return x+y

# 手动装饰
# sayProxy = SayHello()
# res = sayProxy(add)
# print(res(1,2))


# @SayHello()
# def mul(x,y):
#     return x * y
#
# print(mul(2,3))


# 参数
# class Proxy1:
#     def __init__(self,msg):
#         self.msg=msg
#     def __call__(self,func):
#         def wrapper(*args,**kwargs):
#             print(f'我要开始{self.msg}计算了')
#             res = func(*args,**kwargs)
#             return res
#         return wrapper
#
#
# @Proxy1('乘法')
# def mul(x,y):
#     return x * y
# print(mul(2,3))

# 多个装饰器



class Proxy1:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f'我要开始计算了proxy1')
            res = func(*args,**kwargs)
            return res
        return wrapper


class Proxy2:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f'我要开始计算了proxy2')
            res = func(*args,**kwargs)
            return res
        return wrapper


@Proxy2()
@Proxy1()
def sub(x,y):
    return x-y

# 输出结果：
# 我要开始计算了proxy2
# 我要开始计算了proxy1
# -1
print(sub(1,2))