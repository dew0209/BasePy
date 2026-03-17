nums1 = [10,30,20,30]

# 输出结果：0
print(nums1.index(10))

# 输出结果：2
print(nums1.count(30))

nums1.reverse()
# 输出结果：[30, 20, 30, 10]
print(nums1)

nums1.sort()
# 输出结果：[10, 20, 30, 30]
print(nums1)

nums1.sort(reverse=True)
# 输出结果：[30, 30, 20, 10]
print(nums1)

# 若列表中的元素：都是字符串，则按照字符串的Unicode编码大小进行排序
nums_str = ['你好啊','爱心','你好']
nums_str.sort()
# 输出结果：['你好', '你好啊', '爱心']
print(nums_str)


# 报错：若列表中的元素：既有数字，又有字符串，那就会报错
nums2 = [10,20,'你好']
nums2.sort()
print(nums2)

# 报错
nums3 = [10,20,[40,30],0]
nums3.sort()
print(nums3)