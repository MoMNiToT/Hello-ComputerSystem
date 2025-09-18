import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.myos import *
from src.process import *

def my_run():
    while process_count() > 0:
        current = process_schedule()
        call = process_step(current)
        if call.syscall == SyscallType.SYS_EXIT:
            process_exit(current)
        elif call.syscall == SyscallType.SYS_WRITE:
            print(call.arg, end='')
        elif call.syscall == SyscallType.SYS_WRITE_DOUBLE:
            print(call.arg * 2, end='')  
    print()