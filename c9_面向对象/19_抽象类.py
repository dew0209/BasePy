from abc import ABC, abstractmethod

# 抽象类是一种不能直接实例化的类，它通常作为"规范"，让子类去继承，并实现其中定义的[抽象方法]
# 继承ABC，@abstractmethod
# 抽象类不能实例化
class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass
    def speak(self):
        print('say')
# 报错
# m1 = MustRun()

class Person(MustRun):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print(f'我叫{self.name},我在奔跑。')

p1 = Person('张三',18)
# 输出结果：我叫张三,我在奔跑。
p1.run()
# 输出结果：say
p1.speak()