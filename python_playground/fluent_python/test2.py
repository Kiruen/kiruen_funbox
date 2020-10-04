import sys
import os
import psutil
import gc

# 注意管理员身份打开
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


show_memory_info('init')
a = [i for i in range(1, 1000000)]
print(sys.getrefcount(a))
show_memory_info('after')
del a
gc.collect()
show_memory_info('after')
print(a)
