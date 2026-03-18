msg = 'aaaa world'
# 输出结果：d
print(msg[-1])

# 报错
#msg[0] = '1'

# 输出结果：8
print(msg.index('l'))
# 输出结果：2
print(msg.count('aa'))
# 输出结果：['', '', '', '', ' world']
print(msg.split('a'))
# 输出结果：AAAA world
print(msg.replace('a','A'))
# 输出结果：AAAA world
print(msg.replace('aa','AA'))

msg1 = '1234您1好2呀4321'
# 输出结果：您1好2呀
print(msg1.strip('1234'))


msg2 = ' 您 好  '
# 输出结果：您 好
print(msg2.strip()) # 默认删除空格