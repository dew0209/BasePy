class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # 实例方法
    # 自定义方法（给实例添加行为）
    def speak(self,msg):
        print(f"我是{self.name},我想说{msg}")

p1 = Person('张三',12)
p2 = Person('李四',22)

# 输出结果：{'name': '张三', 'age': 12}
print(p1.__dict__)

# 输出结果：我是张三,我想说你好
p1.speak('你好')

# 输出结果：我是李四,我想说你好
Person.speak(p2,'你好')