class Person:
    def __init__(self,name,age,idcard):
        self.name=name # 公有属性：当前类中，子类中，类外部，都可以访问
        self._age=age   # 受保护的属性：当前类，子类中，都可以访问
        self.__idcard = idcard # 私有属性：仅能在当前类中访问
    def speak(self):
        print(f'我叫：{self.name},年龄：{self._age},身份证：{self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是学生：{self.name},年龄：{self._age},身份证：{self.__idcard}')
p1 = Person('张三',22,'212222222222')
# 当前类都能访问
# 输出结果：我叫：张三,年龄：22,身份证：212222222222
p1.speak()


# 报错：__idcard不能访问
# s1 = Student('小明',22,'323232')
# s1.hello()

print(p1.name)
# 不报错：22，在类的外部，如果强制访问[受保护的属性]也能访问到，但十分不推荐
print(p1._age)
# 报错：在类的外部，如果强制访问[私有属性]不能访问到，而且会报错
# print(p1.__idcard)

# Person底层是通过重命名的方式，实现私有属性的
# 输出结果：{'name': '张三', '_age': 22, '_Person__idcard': '212222222222'}
print(p1.__dict__)
# 输出结果：212222222222  不推荐这样访问
print(p1._Person__idcard)

print(Student.__dict__)