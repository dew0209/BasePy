# 所有类都继承了object类

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
# 输出结果：True
print(issubclass(Person,object))
# 输出结果：True
print(issubclass(object,object))
# 输出结果：True
print(issubclass(int,object))
# 输出结果：True
print(issubclass(str,object))
# 输出结果：True
print(isinstance({'吃饭','睡觉'},object))

# 所有对象都继承了object类所提供的：各类属性和方法，从而保证了每个对象都具备统一的基本能力

# 输出结果：
"""
__new__
__repr__
__hash__
__str__
__getattribute__
__setattr__
__delattr__
__lt__
__le__
__eq__
__ne__
__gt__
__ge__
__init__
__reduce_ex__
__reduce__
__getstate__
__subclasshook__
__init_subclass__
__format__
__sizeof__
__dir__
__class__
__doc__
"""
for key in object.__dict__:
    print(key)

p1 = Person('张三',22)
# 输出结果：['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
# 对象可以访问到的东西（自己的，继承过来的）
print(dir(p1))