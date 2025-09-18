import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.process import Process

def priority_scheduler(procs: list[Process]) -> Process:
    max_proc = max(proc.priority for proc in procs)
    for proc in procs:
        if proc.priority == max_proc:
            return proc
    raise NotImplementedError("priority_scheduler is not implemented yet")
