# 占位符精度控制

name = '张三'
age = 20
weight = 65.45
# 输出结果：我叫张   ，我 0020了，体重： 65.5
info = '我叫%-4.1s，我%5.4d了，体重：%5.1f'%(name,age,weight)

print(info)