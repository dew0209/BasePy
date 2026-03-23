# 多态：同一个方法名，在不同的对象上调用时，呈现出不同的行为
# 标准多态 和 鸭子多态
class Animal:
    def speak(self):
        print('动物正在发出声音')

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')


class Pig():
    def speak(self):
        print('哼哼哼')

def make_sound(animal:Animal):
    # 多态的体现
    animal.speak()

a = Animal()
d = Dog()
c = Cat()
p = Pig()

# 输出结果：
"""
汪汪汪
动物正在发出声音
喵喵喵
"""
make_sound(a)
make_sound(d)
make_sound(c)

# 输出结果：哼哼哼
# 此行代码如果在其它语言中会报错，py不会，不推荐这样写
make_sound(p)