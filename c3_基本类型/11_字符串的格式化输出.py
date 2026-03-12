# 字符串的格式化输出

name = '张三'
age = 20
weight = 65.2

# 写法一：只能字符串拼接，浮点和整型都不行
# info = '我叫' + name + ' 我' + age + '了'

# 写法二：占位符，%s 万能 %d或%i 整型 %f 浮点
info2 = '我叫%s，我%i了，体重：%f'%(name,age,weight)
# 输出结果：我叫张三，我20了，体重：65.200000
print(info2)

# 写法三：使用f-string
# 输出结果：我叫张三，我20了，体重：65.2
info3 = f'我叫{name}，我{age}了，体重：{weight}'
print(info3)



