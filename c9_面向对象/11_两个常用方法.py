
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Student(Person):
    def __init__(self,name,age,stu_id):
        # 方式一
        # super().__init__(name,age)
        # 方式二：
        Person.__init__(self,name,age)
        self.stu_id = stu_id

p1 = Student('张三',20,'777189')
# isinstance(instance,Class)：判断某个对象是否为指定类或其子类的实例
# 输出结果：True
print(isinstance(p1,Student))

# issubclass(class1,class2)：判断class1类是否是另一个class2类的子类
# 输出结果：True
print(issubclass(Student,Person))
# 输出结果：False
print(issubclass(Person,Student))