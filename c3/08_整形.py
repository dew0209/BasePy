# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更加易读
import sys

salary = 200_100_299
print(salary)

sys.set_int_max_str_digits(10000)

