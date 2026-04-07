# 方式一：
class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self,person):
        self.index=0
        self.listItem = [person.name,person.age,person.gender,person.address]
    def __next__(self):
        if self.index >= len(self.listItem):
            raise StopIteration
        value = self.listItem[self.index]
        self.index+=1
        return value

p = Person('张三',12,'男','合肥市')
for i in p:
    print(i)
