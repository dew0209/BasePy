age = input('请输入你的年龄：')
if int(age) >= 18:
    print('你是成年人')
elif 0 < int(age) < 18:
    print('你是未成年人')
    print('努力学习，未来可期')
else:
    print('非碳基生物')
    print('异世界入侵')

print('欢迎来到python世界')