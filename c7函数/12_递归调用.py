total = 0

def calc(n):
    """
    方法的注释
    :param n:
    :return:
    """
    if n > 0:
        global total
        total += n
        calc(n - 1)

calc(10)
print(total)