def outer():
    num = 10
    # print(hex(id(num)))
    def inner():
        nonlocal num
        num += 1
        print(num)
    return inner

f = outer()
# f()
# f()
# 闭包：内层函数 + 被内层函数所引用的外层变量
# 闭包产生的条件：
#   1.要有函数嵌套
#   2.在[内层函数]中，要访问[外层函数]的变量
#   3.并且[外层函数]要返回[内层函数]
# 结论：
# 1.outer函数中：被inner所使用到的那些变量，会被封存到闭包单元（cell）中
# 2.这些cell会组成一个__closure__元组，最终放在了 inner 函数上
# (<cell at 0x000002686E7C2230: int object at 0x00007FFCD0A555D8>,)

# 打印__closure__元组
print(f.__closure__)

# 打印__closure__元组中的某一项
print(f.__closure__[0])

# 打印__closure__元组中的某一项的具体值
# 输出结果：10
print(f.__closure__[0].cell_contents)

# 注意点：
# 1.调用n层外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响
f1 = outer()
f2 = outer()
# 输出结果：11
f1()
# 输出结果：12
f1()
# 输出结果：11
f2()
# 2.内层函数中用到的外层变量是可变对象，多个闭包之间依然互不影响
def outer1():
    nums = []
    def inner(value):
        nums.append(value)
        print(nums)
    return inner

f1 = outer1()
f2 = outer1()
# 输出结果：[20]
f1(20)
# 输出结果：[20, 30]
f1(30)
# 输出结果：[2]
f2(2)

# 闭包的优点
"""
1.可以记住状态，不用全局变量，也不用写类，就能在多次调用之间保存数据
2.可以做配置过的函数，先传一部分参数，把环境固定住，得到一个定制版函数
3.可以实现简单的数据隐藏，外层变量对外不可见，只能通过内层函数访问
4.是装饰器等高级用法的基础
"""
# 第二点解释:char 和 n 固定了（先传一部分参数），后续传msg就行
def beaut(char,n):
    def how_msg(msg):
        print(char * n + msg + char * n)
    return how_msg
# 闭包的缺点
"""
1.理解成本较高：对初学者不太友好，滥用会让代码难度
2.如果闭包里引用了很大的对象，又不长期释放，可能会增加内存占用
3.很多场景下，其实用[类 + 实例属性]会更清晰，闭包不一定是最优解
"""