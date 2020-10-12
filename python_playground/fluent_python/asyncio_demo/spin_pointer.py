'旋转指针模块'
__author__ = 'Kiruen'

import sys, threading, time, itertools


class signal:
    '简单的线程通信信号'
    go_on = True


def spin(n: int, sig: signal):
    "指针旋转控制函数"
    write, flush = sys.stdout.write, sys.stdout.flush
    pointers = '-\\|/-\\|/'
    length= len(pointers)
    for ch in itertools.cycle(pointers):
        write(ch)
        flush()
        time.sleep(.5)
        write('\x08' * len(ch))

        if sig.go_on is False:
            break


def supervisor():
    """文档字符串：监视器函数"""
    sig = signal()
    thread = threading.Thread(target=spin, args=(2, sig,))
    thread.start()
    thread.join()


if __name__ == '__main__':
    supervisor()
    # print(dir())
