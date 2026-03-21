class Person:
    # max_age，planet都是类属性，类属性都是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = '地球'
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = Person('张三',22)
p2 = Person('张三',22)

# 验证：实例身上没有类属性
# 输出结果：{'__module__': '__main__', '__firstlineno__': 1, 'max_age': 120, 'planet': '地球', '__init__': <function Person.__init__ at 0x0000016623107110>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
print(Person.__dict__)
# 输出结果：{'name': '张三', 'age': 22}
print(p1.__dict__)
# 输出结果：120。查找过程：自身实例->类上找
print(p1.max_age)

# 进行[实例.属性名 = 值]操作时，只会对实例自身的属性起作用，不会影响类属性
p1.planet = '火星'
# 输出结果：火星
print(p1.planet)
# 输出结果：{'name': '张三', 'age': 22, 'planet': '火星'}
print(p1.__dict__)
# 输出结果：地球
print(p2.planet)
