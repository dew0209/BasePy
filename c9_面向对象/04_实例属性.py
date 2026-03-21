class Person:
    def __init__(self,name,age):
        # 通过[实例.属性名 = 值]给实例添加的属性，就叫实例属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己独一份的实例属性，各个实例之间是互不干扰的
        self.name=name
        self.age=age

p1 = Person('张三',22)

p1.address = '合肥'

# 输出结果：{'name': '张三', 'age': 22, 'address': '合肥'}
print(p1.__dict__)

# 报错
#print(Person.name)