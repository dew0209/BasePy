# 包概述
# 1.在py中。包含__init__.py的文件夹就是一个包（package）
# 2.我们通常会把[某个特定功能相关的所有模块]放入一个包中
# 3.使用包可以进一步提升代码的：可维护性，可复用性，便于管理大型项目

# 包与模块的关系
# 1.一个模块就是一个.py文件，包是用来“管理模块”的目录（文件夹）
# 2.一个包中可以有多个模块，也可以有多个子包
# 包的分类：
# 标准库包，自定义包，第三方包

# 包命名注意点：
# 1.要符合标识符命名规范
# 2.包区分大小写（建议全部使用小写字母）
# 3.不要与标准库包同名


# 常见的包导入方式：
# 1.import 包.模块名
# 2.import 包.模块名 as 别名
# 3.from 包.模块名 import 具体内容1,具体内容2,...
# 4.from 包.模块名 import 具体内容1 as 别名1,具体内容2 as 别名2,...
# 5.from 包.模块名 import *
# 6.from 包 import 模块名
# 7.from 包 import 模块名 as 别名
# 下面这个比较特殊 要和 __init__.py结合
# 8.from 包 import *

# 关于 __init__.py文件
# 1.__init__.py 是包的初始化文件，在包被导入时，__init__.py会被自动调用
# 2.__init__.py 中可以编写一些包的初始化逻辑
# 3.__init__.py 中所定义的内容，会被[from 包名 import *]形式全部引入
# 4.__init__.py 中也可以使用 __all__来控制那些包中的那些模块可以被[from 包名 import *]引入



# import trade.order
# trade.order.create_order()
#
# import trade.order as dd
# dd.create_order()

#
# from trade import *
#
# print(a)
# print(b)
#
# order.create_order()


# 标准库包
from collections import Counter
names = ['张三','李四','张三']
print(Counter(names))