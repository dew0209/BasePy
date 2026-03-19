d1 = {'张三':12,'李四':14}


# 输出结果：张三: 12李四: 14
for key in d1:
    print(f'{key}: {d1[key]}',end='')
print()

# 利用了解包的特性
# 输出结果：张三 12李四 14
for k,v in d1.items():
    print(k,v,end='')