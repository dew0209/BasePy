# keys方法：用于获取字典中所有的键
d1 = {'张三':12,'李四':14}

re = d1.keys()
# 输出结果：<class 'dict_keys'> dict_keys(['张三', '李四'])
print(type(re),re)

# dict_keys可以被遍历，但是不能通过下标访问
# 输出结果：张三 李四
for i in re:
    print(i,end=' ')
print()

# 借助内置的list函数，可以将dict_keys转化为list
res = list(re)
# 输出结果：<class 'list'> ['张三', '李四']
print(type(res),res)

# values方法：获取字典中所有的值
re = d1.values()
# 输出结果：<class 'dict_values'> dict_values([12, 14])
print(type(re),re)

# 输出结果：12 14
for i in re:
    print(i,end=' ')
print()

res = list(re)
# 输出结果：<class 'list'> [12, 14]
print(type(res),res)

# items方法：获取字典中所有的键值对，以元组的形式
ans = d1.items()
# 输出结果：<class 'dict_items'> dict_items([('张三', 12), ('李四', 14)])
print(type(ans),ans)
# 输出结果：('张三', 12) ('李四', 14)
for i in ans:
    print(i,end=' ')