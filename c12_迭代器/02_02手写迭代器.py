# 方式二：这个不太完美，
"""
for i in p:
    for j in p
        xxxxx
有问题，会重置。

"""
class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
        self.__listItem = [name,age,gender,address]
    def __iter__(self):
        self.__index = 0
        return self
    def __next__(self):
        if self.__index >= len(self.__listItem):
            raise StopIteration
        val = self.__listItem[self.__index]
        self.__index += 1
        return val

p = Person('张三',12,'男','合肥市')
for i in p:
    print(i)
print()
for i in p:
    print(i)