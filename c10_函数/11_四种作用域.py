a = 100

def test():
    # 外层作用域
    e = 100
    print('我是test函数')
    print('test中打印的a是',a)
    def inner():
        # 局部作用域
        nonlocal e
        e = 400
        print('inner')