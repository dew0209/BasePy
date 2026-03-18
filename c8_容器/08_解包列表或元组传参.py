def test(data):
    print(f'我是test函数，我收到的参数是{data}')


def test1(*args):
    print(f'我是test函数，我收到的参数是{args},类型：{type(args)}')

list1 = [100,200,300]
tuple1 = ('您好','北京')

# 输出结果：我是test函数，我收到的参数是[100, 200, 300]
test(list1)
# 输出结果：我是test函数，我收到的参数是('您好', '北京')
test(tuple1)

# *解包：把每个元素都依次传进去，test1(*list1)相当于test1(100,200,300)
# 输出结果：我是test函数，我收到的参数是('您好', '北京'),类型：<class 'tuple'>
test1(*list1)
# 输出结果：我是test函数，我收到的参数是(100, 200, 300),类型：<class 'tuple'>
test1(*tuple1)