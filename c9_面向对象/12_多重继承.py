
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f'我是{self.name}')
class Worker:
    def __init__(self,company):
        self.company=company
    def do_work(self):
        print(f'我在{self.company}做兼职')

class Student(Person,Worker):
    def __init__(self,name,age,company,stu_id):
        Person.__init__(self,name,age)
        Worker.__init__(self,company)
        self.stu_id = stu_id
    def study(self):
        print(f'我的学号是{self.stu_id}')


s1 = Student('张三',18,'麦当劳','20260101')

# 输出结果：
# 我是张三
# 我的学号是20260101
# 我在麦当劳做兼职
s1.speak()
s1.study()
s1.do_work()

# 类的_mro_属性：用于记录属性和方法的查找顺序
# 通过实例去查找属性或方法时，会现在实例自身上去查找，如果没有，就按照__mro__记录的顺序去查找
# 输出结果：(<class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Worker'>, <class 'object'>)
print(Student.__mro__)