import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def my_run():
    current = process_schedule()
    new_syscalls = current.syscalls.copy()  # 复制系统调用列表
    new_process = Process(new_syscalls)     # 创建新进程
    new_process.step = current.step         # 复制执行步骤
    process_push(new_process)               # 新进程加入列表末尾
    raise NotImplementedError("my_run function is not implemented yet.")