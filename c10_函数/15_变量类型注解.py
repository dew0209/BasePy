# 类型注解
# 变量类型注解：给变量加上类型说明，可增强代码的可读性，让IDE的提示更友好
# num:int = 100
# # 软约定，实际执行也行
# num = '你好'
# # 输出结果：你好
# print(num)

nums:int = 100
price:float = 12.5
message:str = 'hello'
result:None = None

# 注意：可以先写变量的类型注解，以后再复制
school:str
# 报错：此时变量没有创建的
# print(school)
print("******")
# school此时创建
school = '哈哈哈'
# 输出结果：哈哈哈
print(school)

hobby:list[str] = ['抽烟','喝酒','烫头']
# 3.10版本才行
hobby1:list[str | int] = ['抽烟','喝酒','烫头',12,3]
# 旧版本
from typing import Union
hobby2:list[Union[str, int]] = ['抽烟','喝酒','烫头',12,3]

citys:set[str] = {'北京','上海'}



citys1:set[str | float | bool] = {'北京','上海',False,True}

person:dict[str,int] = {'张三':18,'李四':19}
person1:dict[str | int,int] = {'张三':18,'李四':19,1:1}

# 和上面不一样，tuple是不可变类型，tuple[int]里面只能有一个元素
scores:tuple[int] = (60,)

scores1:tuple[int,int,int] = (60,90,10)
scores2:tuple[int,...] = (60,90,10,20,30)
scores3:tuple[int | str,...] = (60,90,10,20,30,'90')

# py会根据初始赋值推导变量的类型：
# 1.对于普通变量：后续如果改变类型，不会警告
# 2.对于容器变量：要求内部元素必须与推导出来的一直，否则就会警告

# 无警告
a = 1
print(a)
a = '*'

# 有警告
res = [1,2,3]
res.append('2')


# 函数类型注解