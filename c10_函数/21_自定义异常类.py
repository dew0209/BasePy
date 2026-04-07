# 自定义异常类
# 1.由开发人员自己定义一个异常类，用来表示代码中 "更具体，更有业务含义" 的异常类
# 2.具体规则：定义一个类（类名通常以 Error 结尾），继承 Exception 类或它的子类
class CustomerError(Exception):
    def __init__(self,value):
        super().__init__('自定义异常 ： ' + value)


raise CustomerError('测试')