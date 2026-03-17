# c新增
# 方式一：
nums = [10,20]
nums.append(30)
# 输出结果：3
print(len(nums))
# 方式二：
nums1 = [10,20]
nums1.insert(0,30)
# 输出结果：30
print(nums1[0])
# 输出结果：10
print(nums1[1])
# 方式三：
nums2 = [10,20]
nums2.extend([30,'你好'])
nums2.extend('你好')
# 输出结果：[10, 20, 30, '你好', '你', '好']
print(nums2)

# D:删除
# 方式一：
nums3 = [10,20]
# 输出结果：[10, 20]
print(nums3)
res = nums3.pop(0)
# 输出结果：10
print(res)
# 输出结果：[20]
print(nums3)

# 方式二：
nums4 = [10,20]
nums4.remove(20)
# 输出结果：[10]
print(nums4)

# 方式三：
nums5 = [10,20]
nums5.clear()
# 输出结果：[]
print(nums5)

# 方式四
nums6 = [10,20]
del nums6[0]
# 输出结果：[20]
print(nums6)

# u:修改
nums7 = [10,20]
nums7[0] = 30
# 输出结果：[30, 20]
print(nums7)

# R:查询
nums8 = [10,20]
# 输出结果：10
print(nums8[0])