def info(msg):
    return '[提示]: ' + msg

def warn(msg):
    return '[警告]: ' + msg

def error(msg):
    return '[错误]: ' + msg

def log(func,text):
    print(func(text))

# 输出结果：
# [提示]: 成功
# [错误]: 异常
log(info,'成功')
log(error,'异常')