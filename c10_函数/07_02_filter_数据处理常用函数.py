# filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据
#	filter(过滤函数,可迭代对象)

# 筛选数值
nums = [10,20,30,40]

res = filter(lambda n : n > 20,nums)
# 输出结果：[30, 40]
print(list(res))
# 输出结果：<class 'filter'>
print(type(res))

data = [0,1,'','hello',[],(),5]
res = filter(None,data)
# 输出结果：[1, 'hello', 5]
print(list(res))