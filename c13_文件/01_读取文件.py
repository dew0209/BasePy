""""""

"""
读取文件的标准流程：
    1.创建文件对象
    2.操作文件（读取，写入等）
    3.关闭文件
"""

"""
open函数
    参数：
        1.file：要操作的文件路径
        2.mode：文件的打开模式
            r：读取（默认值）
            w：写入，并先截断文件
            x：排它性创建，如果文件已存在，则创建失败
            a：打开文件用于写入，如果文件存在，则在文件末尾追加内容
            b：二进制模式
            t：文本模式（默认值）
            +：打开用于更新（读取与写入）
        3.encoding：字符编码
"""
# region
# # 第一步：创建
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# # 第二步：操作文件
# result = file.read()
# print(result)
# # 第三步：关闭文件
# file.close()
#
# # 第一步：创建
# file = open(file='banner1.png', mode='rb')
# # 第二步：操作文件
# result = file.read()
# print(result)
# # 第三步：关闭文件
# file.close()

# endregion

"""
read 方法说明：
    1.read(size)中的size是可选承诺书
        不传递size参数，表示：读取文件中所有的内容（注意内存占用）
        传递了size参数，表示：读取文件中指定个数的字符，或指定大小的字节
    2.read会从上一次read的位置继续读取（指针思想），若到达文件末尾后继续读取，将返回空字符串
"""
# region
#
# # 第一步：创建
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# # 第二步：操作文件
# result = file.read(7)
# print(repr(result))
# result = file.read(3)
# print(repr(result))
# # 第三步：关闭文件
# file.close()
#
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# # True
# print(hasattr(file, '__iter__'))
# # True
# print(hasattr(file, '__next__'))

#
# while True:
#     line = file.read(3)
#     if line:
#         print(line, end='')
#     else:
#         break
# file.close()
# 或
#
# for line in file:
#     print(line,end='')
#
# file.close()

# endregion


"""
readline:
    1.readline(size):
        不传递 size 参数，表示：读取当前这一行所有的内容
        传递 size 参数，表示：读取当前行时，最多能读取的字符数，或字节数（size不是行数）
    2.readline方法，也是从上一次位置继续读取，若到达文件末尾后继续读取，也是返回空字符串
"""
# region
# # 第一步：创建
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# # 第二步：操作文件
# result = file.readline(3)
# print(result,end='')
# result = file.readline(3)
# print(result,end='')
# # 莫愁前路无知己\n只有八个，到这里已经九个了，不会输出”天”。
# # 己\n
# result = file.readline(3)
# print(repr(result),end='')
# result = file.readline(3)
# print(result,end='')
# # 第三步：关闭文件
# file.close()
# endregion


"""
使用for循环直接遍历文件对象
"""
# region
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# for line in file:
#     print(line,end='')
# file.close()
# endregion

"""
readlines 方法，一次性按行读完，返回一个列表
    1.readdlines(hint)中的hint是可选参数
        不传递hint参数，表示：读取当前文件的所有行
        传递hint参数，表示：期望读取的[字符个数 或 字节数的上限]（hint不是行数）
        至少读取到一行的末尾
    2.由于 readlines是一次性读取文件的所有内容，所以不适合读取体积较大的文件
"""
# region
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# result = file.readlines(3)
# # ['莫愁前路无知己\n']
# print(result)
# endregion

"""
最佳实践：with上下文管理器，结合for循环，逐行读取文件
结束后会自动关闭文件 
"""
with open(file='a.txt', mode='rt', encoding='utf-8') as file:
    for line in file:
        print(line,end='')