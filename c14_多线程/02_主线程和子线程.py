""""""
import os
import time

"""
windows查看ParentPid，pid命令
wmic process get Name,ParentProcessId,processId
"""

print(f'当前进程的pid:{os.getpid()}')
print(f'当前进程的父进程pid:{os.getppid()}')

time.sleep(10000)