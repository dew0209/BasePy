class Person:
    def __init__(self,name,age,idcard):
        self.name=name # 公有属性：当前类中，子类中，类外部，都可以访问
        self._age=age   # 受保护的属性：当前类，子类中，都可以访问
        self.__idcard = idcard # 私有属性：仅能在当前类中访问
    # 注册age属性的getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age
    # 注册age属性setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
    @age.setter
    def age(self,age):
        self._age=age

p1 = Person('张三',22,'212222222222')

# 输出结果：22
print(p1.age)
p1.age = 20
# 输出结果：20
print(p1.age)