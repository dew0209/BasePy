total = 0

def calc(n):
    if n > 0:
        global total
        total += n
        calc(n - 1)

calc(10)
print(total)