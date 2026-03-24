# 1.函数的多返回值
def calc(x,y):
    res1 = x + y
    res2 = x - y
    res3 = x * y
    return res1, res2, res3
res = calc(3,4)
# 输出结果：(7, -1, 12)
print(res)


# 2.参数的打包与解包
# 打包接受参数
# *（元组） 和 **（字典）

def show_info(*qew,**asd):
    print(qew)
    print(asd)
# 输出结果：
# (10, 20, 30)
# {'name': '张三', 'age': 21}
show_info(10,20,30,name='张三',age=21)


# 解包传递参数
# *变量名：将元组或列表拆解一个一个独立的位置参数
# **变量名：将字典拆解一个一个 key=value 形式的关键字参数
def show_info1(num1,num2,name,age):
    print(num1,num2,name,age)
nums = {10,20}
person = {'name':'张三','age':12}
# 输出结果：10 20 张三 12
show_info1(*nums,**person)


# 混合一起使用
def show_info3(*qew,**asd):
    print(qew)
    print(asd)
nums = {10,20}
person = {'name':'张三','age':12}
# 输出结果：
# (10, 20)
# {'name': '张三', 'age': 12}
show_info3(*nums,**person)