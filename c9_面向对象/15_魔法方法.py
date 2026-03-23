# 概念：以__xxx__命名的特殊方法(双下划线开头和结尾)
# 特点：不需要我们手动调，我们只要准备好这些方法，Python会在特定场景下，去自动调用


class Person:
    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f'[{self.name},{self._age},{self.__idcard}]'
    def __len__(self):
        return len(p1.__dict__)
    def __lt__(self, other):
        return self._age < other.age
    def __gt__(self, other):
        return self._age > other.age
    def __eq__(self, other):
        return self._age == other.age
    def __getattr__(self, item):
        return f'您访问的{item}不存在'

p1 = Person('张三',22,'212121')

# 输出结果：[张三,22,212121]
# 默认调用：__str__()
print(p1)

# 输出结果：3
# 默认调用：__len__()
print(len(p1))


p2 = Person('李四',33,'3333')

# 输出结果：True
# 默认调用:p1.__lt__(p2)
print(p1 < p2)

# 输出结果：False
# 默认调用:p1.__gt__(p2)
print(p1 > p2)


# 输出结果：False
# 默认调用:p1.__eq__(p2),不重写，比较的是地址
print(p1 == p2)

# 输出结果：您访问的address不存在
# address不存在，调用__getattr__
print(p1.address)

