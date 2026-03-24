# 将每个数变成原来的2两倍
list1 = [1,2,3,4]

# 方式一：
res = map(lambda x:x*2,list1)
# 输出结果：[2, 4, 6, 8]
print(list(res))

# 方式二：
res = [item * 2 for item in list1]
# 输出结果：[2, 4, 6, 8]
print(res)

# 只拿大于五的
res = [item * 2 for item in list1 if item * 2 > 5]
# 输出结果：[6, 8]
print(res)

# 字典推导式
name = ['张三','李四','王五']
scores = [60,70,80]
# 输出结果：{'张三': 60, '李四': 70, '王五': 80}
res = {name[i]:scores[i] for i in range(len(name))}
print(res)

# 集合推导式
name = ['张三','李四','王五']
res = {n + '!' for n in name}
# 输出结果：{'王五!', '李四!', '张三!'}
print(res)

# 没有元组推导式
name = ['张三','李四','王五']
# 这个是生成器，不是元组
res = (n + '!' for n in name)
print(res)