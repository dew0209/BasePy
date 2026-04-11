""""""
import os
import shutil
"""
1.os.mkdir(path):创建单级目录（如果目录已经存在，则会抛出异常）
2.os.makedirs(path):创建多级目录（如果路径中的所有目录都已经存在，则会抛出异常）
3.os.rmdir(path):删除空目录（如果目录不存在，或目录非空，都会抛出异常）
4.os.removedirs(path):递归删除空目录，在成功删除末尾一级目录后，会”向上“尝试把父级目录也删除（直到父目录不是空目录）
5.os.path.exists(path):判断路径是否存在（文件/目录都算）
6.os.path.isdir(path):用于判断路径，具体规则如下
    路径不存在，返回False
    路径存在，但是指向的是文件False
    路径存在，并且是目录True
7.os.path.isfile(path):判断是否为文件
8.os.scandir(path):扫描指定目录
9.os.walk(path):按层级，递归遍历指定目录下，所有的子目录和文件
10.shutil.rmtree(path):删除有内容的目录

"""
# region
# os.mkdir('aaa')
# res = os.scandir('./')
# for item in res:
#     print('目录' if item.is_dir() else '文件',item.name)
# endregion