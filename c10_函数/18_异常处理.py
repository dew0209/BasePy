# 1.将可能出现异常的代码放在 try 中，出现异常后的处理代码写在 except 中
# 2.如果 try 中的代码出现异常，那 try 中的后续代码将不会执行，并自动跳转到 except 中处理异常
# 3.如果 try 中的代码没有异常，那 except 中的代码就不会执行
# 4.无论是否发生异常，try-except 后面的代码都会继续执行
#
# try:
#     a = 1
#     b = int(input('请输入b'))
#     res = a / b
# except (ZeroDivisionError,ValueError) as e:
#     # print('异常')
#     # print(f'出现异常了{e}')
#     # print(f'出现异常了{type(e)}')
#     # print(f'出现异常了{e.args}')
#     # print(f'出现异常了{type(e.args)}')
#     if isinstance(e, ZeroDivisionError):
#         print('除0异常')
#     if isinstance(e, ValueError):
#         print('数值异常')
# except Exception as e:
#     print(f'兜底:{e.args}')
#
#
# print('结束')
import traceback

# 完整写法
# 1.try：尝试去做可能会出现异常的事情
# 2.except：出现异常时的处理（出现异常时怎么补救）
# 3.else：如果一切顺利（没有出现异常）要做的事情
# 4.finally:无论有没有异常，都要做的事

try:
    print('try')
    res = 1 / 0
except Exception as e:


    print(f'异常信息{e.args}')
    # 格式化好的异常信息
    # 通过 traceback 来回溯异常
    import traceback
    print(traceback.format_exc())

else:
    print('无异常')
finally:
    print('完整实现结束')