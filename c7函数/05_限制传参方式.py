
def order(a,/,*,b,c):
    print(f'{a},{b},{c}')

# 输出结果：1,2,3
order(1,b=2,c=3)

def order1(a,/,b,*,c):
    print(f'{a},{b},{c}')
# 输出结果：1,2,3
order1(1,b=2,c=3)
# 输出结果：1,2,3
order1(1,2,c=3)

def order2(a,*,b,c):
    print(f'{a},{b},{c}')
order2(1,b = 2,c=3)

