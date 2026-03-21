
class Person:
    plant = '地球'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self,msg):
        print(f'我是{self.name},我想说：{msg}')


# 继承
class Student(Person):
    def __init__(self,name,age,stu_id):
        # 方式一
        # super().__init__(name,age)
        # 方式二：
        Person.__init__(self,name,age)
        self.stu_id = stu_id
    def study(self,msg):
        print(f'我叫{self.name},我在学{msg}')

s1 = Student('张三',22,'5180209')

# 输出结果：{'name': '张三', 'age': 22, 'stu_id': '5180209'}
print(s1.__dict__)
# 输出结果：<class '__main__.Student'>
print(type(s1))

def speck(data):
    print(f'我是s1自身的speak方法,{data}')

# 查找speak方法的过程：实例自身->student类->person类
# 输出结果：我是张三,我想说：您好
s1.speak('您好')
s1.speak = speck
# 输出结果：我是s1自身的speak方法,哈哈哈
s1.speak('哈哈哈')

# 查找study方法的过程：自身实例->student类->person类
# 输出结果：我叫张三,我在学数学
s1.study('数学')