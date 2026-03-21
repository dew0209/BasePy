class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 自定义方法（给实例添加行为）
    # speak方法只有一份，保存在Person上，所有的Person类的实例对象，都可以调用到是speak方法
    def speak(self,msg):
        print(f'{self.name} say {msg} ')

p1 = Person('张三',12)
p2 = Person('李四',22)
# 输出结果：{'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Person.__init__ at 0x000001FF300E7110>, 'speak': <function Person.speak at 0x000001FF300E71C0>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
print(Person.__dict__)
# 输出结果：{'name': '张三', 'age': 12} 没有speak方法
print(p1.__dict__)
# 输出结果：{'name': '李四', 'age': 22} 没有speak方法
print(p2.__dict__)
# 查找speak的方法的过程：1.实例对象自身->2.到类上去找
# 输出结果：张三 say hello 你好
p1.speak('hello 你好')
# 输出结果：李四 say hi
p2.speak('hi')

def speak():
    print('哈哈哈哈')

p1.speak = speak
# 输出结果：哈哈哈哈
p1.speak()