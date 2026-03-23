# 如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
# 鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否”做某件事“（是否有对应方法）


class Dog():
    def speak(self):
        print('汪汪汪')

class Cat():
    def speak(self):
        print('喵喵喵')


class Pig():
    def speak(self):
        print('哼哼哼')


class Fish():
    def speak(self):
        print('咕噜噜')

def make_sound(animal):
    # 多态的体现
    animal.speak()

d = Dog()
c = Cat()
p = Pig()
f = Fish()

# 输出结果：
"""
汪汪汪
喵喵喵
哼哼哼
咕噜噜
"""

make_sound(d)
make_sound(c)
make_sound(p)
make_sound(f)