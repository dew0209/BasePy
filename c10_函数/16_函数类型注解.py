# 函数类型注解：给函数的参数和返回值添加类型说明
# 函数名(参数1:类型,参数2:类型) -> 返回值类型

def add(a:int,b:int) -> int:
    return a+b
print(add(1,2))

# 参数有默认值的话，py可以推导出参数的类型，设置返回值类型
def add1(x = 1,y = 2)->int:
    return x+y

# 有警告
# add1('1',2)


def add2(*args:int)->int:
    return sum(args)


print(add2(10, 20))


def show(**args:int | str):
    print(args)


show(name='张三',age=18)

# 获取函数的注解信息
# 输出结果：{'args': int | str}
print(show.__annotations__)