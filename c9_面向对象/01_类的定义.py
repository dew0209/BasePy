# 类名通常使用：大驼峰写法
class Person:
    # 初始化方法：类似java的构造方法，self是当前正在创建的实例对象，创建实例对象的时候，Python会自动调用其__init__方法
    def __init__(self,name,age):
        self.name=name
        self.age=age