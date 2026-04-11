# 1.复制
import time

with open('banner1.png','rb') as source,open('banner2.png','wb') as target:
    while True:
        res = source.read()
        if not res:
            break
        target.write(res)

# 2.日志

users = {
    '张三':'1234',
    '李四':'1234vc',
    '王五':'1234ab'
}

def log(msg):
    with open('log.txt','at',encoding='utf-8') as f:
        f.write(msg + '\n')

username = input('请输入用户名：')
password = input('请输入密码：')

nowtime = time.strftime('%Y-%m-%d %H:%M:%S')

if username not in users:
    print('用户名未注册')
    log(nowtime + ' ' + username + '用户名未注册')
elif users[username] != password:
    print('密码不正确')
    log(nowtime + ' ' + username + '密码不正确')
else:
    log(nowtime + ' ' + username + '登录成功')
