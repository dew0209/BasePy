from datetime import datetime

class Person:
    plant = '地球'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # 静态方法
    # 使用@staticmethod装饰过的方法，就叫：静态方法，静态方法也是保存在类身上
    # 不会收到self，cls参数
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        return age >= 18
# 输出结果：True
print(Person.is_adult(1999))

# 通过实例也能调用静态方法，但是不推荐