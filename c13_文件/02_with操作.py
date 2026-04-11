""""""
"""
1.python中的with主要用于管理程序中”需要成对出现的操作“
2.最终目标:编码者只管做具体的事情，进入和离开的事情，让python自动处理

3.语法格式如下：
    with 能得到一个上下文管理器的表达式 as 变量:
        具体是事1
        具体是事2
        具体是事3

4.上下文管理器协议：
    __enter__:with中的代码执行之前调用，其返回值会复制给 as 后的变量
    __exit__:with中的代码执行结束后调用（无论是with中是否出现异常都会调用）
    
"""

# region

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f'我叫{self.name},{self.age}岁了')
    def __enter__(self):
        print('我是进入的逻辑')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('我是离开的逻辑')
        """
            exc_type:异常类型
            exc_val:异常对象
            exc_tb:异常追踪信息
            
            当 with 中的代码发生异常时，__exit__方法的返回值规则如下：
                返回True：表示异常已经被处理，异常不会被继续抛出
                返回False：表示异常没有被处理，异常会被继续抛出
        """
        if exc_type:
            print('exc_type',exc_type)
            print('exc_val',exc_val)
            print('exc_tb',exc_tb)
            return False
        return True

with Person('张三',18) as p1:
    print(type(p1))
    p1.speak()
    #1 / 0


with Person('张三',18) as p1,Person('李四',20) as p2:
    p1.speak()
    p2.speak()
# endregion