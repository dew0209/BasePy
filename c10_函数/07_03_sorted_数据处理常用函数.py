# sorted函数:
# 语法：sorted(可迭代对象,key=xxx,reverse=xxx)
nums = [30,40,20,10]
res = sorted(nums,reverse=True)
print(res)

names = ['python','java','sql']
# res = sorted(names,key=lambda n : len(n))
res = sorted(names,key=len)
print(res)

