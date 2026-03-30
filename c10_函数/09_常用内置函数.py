# print()=>输出指定内容
import time

# print(*objects,sep='',end='\n',fil=sys.stdout,flush=False)
#       要输出的内容，分割符，结束符，输出位置，是否立即刷新
# f = open('a.txt','w',encoding='utf-8')
# print(10,20,sep='-',file=f)

# print('加载中',end='',flush=True)
# for i in range(5):
#     print('.', end='')
#     time.sleep(1)
#
# for i in range(1,101):
#     print(f'\r已加载{i}%', end='')
#     time.sleep(0.1)

# 输出结果：9
# print(abs(-9))

# 取整
# 输出结果：4.2.
# 第二个参数是保留的小数位是多少
# print(round(4.25,1))

# 2的2次方 模 5
# 输出结果：4
# print(pow(2,2,5))

# 输出结果：(3, 1)
# print(divmod(10,3))

# 开始（含） 起始（不含） 步长
# for index in range(1,10,2):
#     print(index)
# names = ('张三','李四','王五')
# scores = [60,70,80]
# re = zip(names,scores)
# 输出结果：[('张三', 60), ('李四', 70), ('王五', 80)]
# print(list(re))
# print(tuple(re))
# for name,score in re:
#     print(name,score)

li = [10,'您好',0]

print(all(li))


print(any(li))