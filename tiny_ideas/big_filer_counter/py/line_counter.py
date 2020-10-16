# 工程实践集体面试提的一个很简单的问题，但是以前只是纸上谈兵，从来没真正实现过，所以问到时脑子一片空白，组织不上来语言
import random
import numpy as np
import functools, itertools
import collections as coll
import os
import asyncio, threading, multiprocessing
from concurrent import futures
import shutil

SPLIT_FILE_COUNT = 10


def get_rand_str():
    return ''.join(chr(i) for i in np.random.randint(62, 67, np.random.randint(5, 10)))


def read_file_stub():
    # print(get_rand_str())
    return (get_rand_str() for i in range(10 ** 8))


def my_hash(_str):
    return hash(_str) % SPLIT_FILE_COUNT


def get_relative_name(_str):
    return f"{my_hash(_str)}"


def open_relative_file(_dir, _str, mode='r'):
    filename = get_relative_name(_str)  # 文件内行大于统计值，因为有完全一样的字符串？
    return open_file(_dir, filename, mode)

readfds, writefds = {}, {}
sem = threading.RLock()
def open_file(_dir, filename, mode):
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    path = f"{_dir}\\{filename}.txt"
    if path not in readfds and path not in writefds:
        with sem:
            if mode == 'r' and path not in readfds:
                # sem.acquire()

                print(os.path.abspath('.'))
                print(readfds)
                # open('H:\\test.au3', 'r')
                readfds[path] = open(path, 'r', buffering=1024 * 6)
                # sem.release()
            elif mode == 'a' and path not in writefds:
                # sem.acquire()
                writefds[path] = open(path, 'a', buffering=1024 * 6)
                # sem.release()
    fd = readfds[path] if mode == 'r' else writefds[path]
    fd.seek(0)
    return fd


def proc_temps(filename):
    # with open_file('.\\temp', filename, 'r') as fpr, \
    #         open_file('.\\output', filename, 'a') as fpw:
    fpr = open_file('.\\temp', filename, 'r')
    fpw = open_file('.\\output', filename, 'a')
    lines = fpr.readlines()
    counter = coll.Counter(lines)
    fpw.writelines([f"{v}:   {k}" for k, v in reversed(sorted(counter.items(), key=lambda it: it[1]))])


def big_file_counter():
    if os.path.exists('.\\temp'):
        shutil.rmtree('.\\temp')
    if os.path.exists('.\\output'):
        shutil.rmtree('.\\output')
    # open_relative_file('.\\temp', 'asfjasi', 'r')

    lines = read_file_stub()
    # counter = coll.Counter()
    # counter = coll.namedtuple('')
    # counter = {}  # {'xxx':(1, code) }
    thread_count, thread_data_size = 12, 100000
    # with futures.ThreadPoolExecutor(thread_count) as executor:
    def proc_input_lines(_lines):
        for line in _lines:
            fp = open_relative_file('.\\temp', line, 'a')
            fp.write(f'{line}\n')

    line_buffer = []
    for line in lines:
        line_buffer.append(line)
        if len(line_buffer) == thread_data_size:
            # proc_input_lines(line_buffer)
            thread = threading.Thread(target=proc_input_lines, args=(line_buffer,))
            thread.start()
            line_buffer.clear()

    # def proc_input(th_i):
    #     for line in itertools.islice(lines, th_i * thread_data_size, (th_i + 1) * thread_data_size - 1):
    #         with open_relative_file('.\\temp', line, 'a') as fp:
    #             fp.write(f'{line}\n')
    # executor.map(proc_input, range(thread_count))
    # pool = multiprocessing.Pool(processes=20)
    # pool.map(proc_input, range(thread_count))
    # pool.join()
    # pool.close()


    with futures.ThreadPoolExecutor(10) as executor:  # 还不能用多进程啊？？因为子进程会重复执行代码。。
        # for i in range(SPLIT_FILE_COUNT):
        #     executor.submit(proc)
        executor.map(proc_temps, [str(code) for code in range(SPLIT_FILE_COUNT)])

    # return counter, coll.Counter([hash(line) % SPLIT_FILE_COUNT for line in counter.keys()])


# 100 * 10 ^ 10 / 4 * 10 ^ 10 = 25个文件

big_file_counter()

# lines = read_file_stub()
# for line in itertools.islice(lines, 1, 10):
#     print(line)
#
# for line in itertools.islice(lines, 10, 20):
#     print(line)

# fd = open('dp_primer.py', 'r', encoding='utf-8')
# print(fd.readlines())
# print(fd.readlines())