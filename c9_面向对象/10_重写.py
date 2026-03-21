
class Person:
    plant = '地球'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self,msg):
        print(f'我是{self.name},我想说：{msg}')


class Student(Person):
    def __init__(self,name,age,stu_id):
        # 方式一
        # super().__init__(name,age)
        # 方式二：
        Person.__init__(self,name,age)
        self.stu_id = stu_id

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会覆盖父类的方法
    def speak(self,msg):
        super().speak(msg)
        print(f'我是学生，我的学号是{self.stu_id}')

# 输出结果：
# 我是张三,我想说：哈哈哈
# 我是学生，我的学号是5180209
s1 = Student('张三',12,'5180209')

s1.speak('哈哈哈')