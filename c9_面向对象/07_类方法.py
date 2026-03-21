class Person:
    plant = '地球'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self,msg):
        print(f"我是{self.name},我想说{msg}")
    # 使用 @classmethod 装饰过的方法，就叫类方法
    # 类方法可以访问类属性
    # cls：当前类本身
    @classmethod
    def test1(cls,msg):
        print(f'您好{cls.plant},信息{msg}',cls)

    @classmethod
    def create(cls,info):
        name,age = info.split('-')
        return cls(name,age)

# 输出结果：{'__module__': '__main__', '__firstlineno__': 1, 'plant': '地球', '__init__': <function Person.__init__ at 0x0000010E1E217110>, 'speak': <function Person.speak at 0x0000010E1E2171C0>, 'test1': <classmethod(<function Person.test1 at 0x0000010E1E217320>)>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
print(Person.__dict__)

p1 = Person('张三',12)

print(p1.__dict__)

# 输出结果：您好地球,信息急啊急啊 <class '__main__.Person'>
Person.test1('急啊急啊')

# 输出结果：{'name': '张三', 'age': '22'}
p1 = Person.create('张三-22')
print(p1.__dict__)