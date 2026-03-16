a = 100
b = 200

def test():
    c = 'hello'
    d = 'world'
    # 声明a是全局中的a
    #global a
    a = 300
    print(a)
    print(b)
    print(c)
    print(d)
test()
print(a)
print(b)
# 报错
# print(c)


# 输出结果：无global时
"""
300
200
hello
world
100
200
"""


# 输出结果：有global时
"""
300
200
hello
world
300
200
"""