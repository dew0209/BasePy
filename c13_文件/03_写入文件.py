# region
# w模式
# with open(file='b.txt', mode='w', encoding='utf-8') as file:
#     file.write('你好')
# endregion
import time

# region
# x模式
# b.txt已经存在，报错
# with open(file='b.txt', mode='xt', encoding='utf-8') as file:
#     file.write('你好')

# with open(file='c.txt', mode='xt', encoding='utf-8') as file:
#     file.write('你好')

# endregion


# region
# a模式

# with open(file='a.txt', mode='at', encoding='utf-8') as file:
#     file.write('你好')

# endregion


# 在python中文件写入时，并不是每写一次就立刻落盘，而是：先写到缓冲区里
# 文件对象中的flush方法：把缓冲区中的数据，立刻写入到文件中
# region
# with open(file='a.txt', mode='at', encoding='utf-8') as file:
#     file.write('21212\n')
#     file.write('21212\n')
#     file.flush()
#     file.write('21212\n')
#     time.sleep(10000)
# endregion

# +:需要搭配其他使用
# 报错
# with open(file='d.txt', mode='+', encoding='utf-8') as file:
#     file.write('你好')

with open(file='d.txt', mode='rt+', encoding='utf-8') as file:
    """
        seek(offset,whence)方法：用于改变对象指针的位置
            offset：偏移量，要移动多少距离。字节便宜
            whence：参考点，从哪里开始计算偏移，有三种取值
                0：从文件开头计算（默认值）
                1：从当前位置
                2：从文件末尾计算
            在文本模式下，不要随着去定位中文字符位置，否则可能破坏文件编码
    """
    file.seek(0,2)
    file.write('你')

