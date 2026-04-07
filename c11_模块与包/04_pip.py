# 全局环境和虚拟环境共享全局环境的标准库，但是不恭喜第三方包
# pip常用命令
# 1.pip install 包名 ：安装指定包
# 2.pip install -i 镜像地址 包名 ： 临时使用镜像地址安装指定包
# 3.pip config set global.index-url 地址：设置pip所使用的镜像地址
# 4.pip config list：查看当前环境的pip配置
# 5.pip config unset global.index-url：让pip回复使用官方默认的地址
# 6.pip list：列出当前环境中，已安装的所有第三方包
# 7.pip uninstall 包名：从当前环境中卸载指定的第三方包
# 全局第三方包文件位置：D:\java\py\Lib\site-packages





# 如何把包安装到当前虚拟环境
# 1.进入.venv\Scripts,执行activate命令，然后开始pip
# 2.pycharm 终端直接打开后执行pip命令
# 3.pycharm 右下角->解释器设置
import numpy

