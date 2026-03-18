list1 = [1,2,3,4,5]
# 输出结果：[1, 2, 3, 4, 5]
print(list1[0:5:1])
# 输出结果：[1, 3, 5]
print(list1[0:5:2])
# 输出结果：[1]
print(list1[0:5:10000000])
# 输出结果：<class 'list'>
print(type(list1[0:5:10000000]))

tuple1 = (1,2,3,4,5)
# 输出结果：(1, 2, 3, 4)
print(tuple1[0:4:1])
# 输出结果：<class 'tuple'>
print(type(tuple1[0:5:1]))


list2 = [1,2,3]
list3 = [4,5,6]
# 输出结果：[1, 2, 3, 4, 5, 6]
print(list2 + list3)
# 输出结果：[1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list2 * 3)
# 输出结果：[]
print(list2 * 0)
# 输出结果：[]
print(list2 * -1)
# 输出结果：[1, 2, 3]
print(list2 * 1)