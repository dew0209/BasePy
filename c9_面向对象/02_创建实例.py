# 类名通常使用：大驼峰写法
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


p1 = Person('张三',12)

# 输出结果：<__main__.Person object at 0x0000020D0C038C20>
print(p1)
# 输出结果：张三
print(p1.name)

# 通过实例.__dict__可以查看实例身上的所有属性
# 输出结果：{'name': '张三', 'age': 12}
print(p1.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address = '合肥'
# 输出结果：{'name': '张三', 'age': 12, 'address': '合肥'}
print(p1.__dict__)

# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
# 输出结果：<class '__main__.Person'>
print(type(p1))