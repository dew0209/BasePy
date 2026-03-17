num1 = [20,10,3]

index = 0
# 输出结果：20 10 3
while index < len(num1):
    print(num1[index],end=' ')
    index += 1

print()
# 输出结果：20 10 3
for item in num1:
    print(item,end=' ')
print()
# 输出结果：20 10 3
for index in range(len(num1)):
    print(num1[index],end=' ')
print()
# 输出结果：2 20 3 10 4 3
for index,item in enumerate(num1,start=2):
    print(index,item,end=' ')
print()

# 没有一个元素，if num2为False
num2 = []
if not num2:
    print('空列表')
print()
