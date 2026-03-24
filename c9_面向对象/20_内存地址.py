a = 66
print(id(a))

b = a
print(id(b))
# 两个地址一样

a = 888
print(id(a))

print(id(b))
# 两个地址不一样，int是不可变对象

# gc
del b



# python中常见的不可变对象有：int,float,bool,str,tuple,frozenset,None
# python中常见的可变对象有：list,dice,set,自定义类的实例对象


stu_list = ['张三','李四','王五']
print(id(stu_list))
stu_list[0] = '张三三'
print(id(stu_list))
# 地址一样
