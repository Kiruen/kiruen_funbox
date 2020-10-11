import numpy as np
import math
import numpy as np
from functools import lru_cache
import sys
import collections as coll

# @lru_cache()
states = np.empty(32, dtype='l')
states[[0, 1]] = 1


def fib(n):
    global states
    if len(states) < n:
        states = states.repeat(2)  # np.concatenate(states, np.empty(n - len(states)))
        states[[0, 1]] = 1
    for i in range(2, n):
        states[i] = states[i - 1] + states[i - 2]
    return states[n - 1]

@lru_cache(maxsize=256)
def get_levens_dis_retro(a, b, i=0, j=0, edist=0):
    # global a, b, min_dist
    me = get_levens_dis_retro
    if not hasattr(me, 'min_dist'):  # 静态变量
        me.min_dist = sys.maxsize

    m, n = len(a), len(b)
    if i == m or j == n:
        if i < m:
            edist += (m - i)
        if j < n:
            edist += (n - j)
        if edist < me.min_dist:
            me.min_dist = edist
        return me.min_dist

    if a[i] == b[j]:
        get_levens_dis_retro(a, b, i + 1, j + 1, edist)
    else:
        get_levens_dis_retro(a, b, i, j + 1, edist + 1)
        get_levens_dis_retro(a, b, i + 1, j, edist + 1)
        get_levens_dis_retro(a, b, i + 1, j + 1, edist + 1)
    return me.min_dist


def get_levens_dis_dp(a, b, i, j):
    pass


'''
a:str "asba"
b:str "astbsa"
'''
@lru_cache(maxsize=128)
def get_max_shared_substr_retro(a, b, i=0, j=0, length=0):
    me = get_max_shared_substr_retro
    if not hasattr(me, 'max_len'):  # 静态变量
        me.max_len = 0

    m, n = len(a), len(b)
    if i == m or j == n:
        if length > me.max_len:
            me.max_len = length
        return me.max_len

    # 总感觉哪里不对，但结果几乎总是正确的
    if a[i] == b[j]:
        get_max_shared_substr_retro(a, b, i + 1, j + 1, length + 1)
    else:
        get_max_shared_substr_retro(a, b, i, j + 1, length)
        get_max_shared_substr_retro(a, b, i + 1, j, length)
        get_max_shared_substr_retro(a, b, i + 1, j + 1, length)
    return a, b, me.max_len


def get_max_shared_substr_dp(a, b, print_indexs=False):
    m, n = len(a), len(b)
    max_sub_indexs = coll.deque()
    max_lens = np.zeros((m, n), dtype='i')
    max_lens[0, 0] = 1 if a[0] == b[0] else 0
    if max_lens[0, 0] == 1:
        max_sub_indexs.append((0, 0))
    for j in range(1, n):
        max_lens[0, j] = 1 if a[0] == b[j] else max_lens[0, j - 1]
    for i in range(1, m):
        max_lens[i, 0] = 1 if a[i] == b[0] else max_lens[i - 1, 0]

    for i in range(1, m):
        for j in range(1, n):
            if a[i] == b[j]:
                max_sub_indexs.append((i, j))
                if print_indexs:
                    print(max_sub_indexs)
                max_lens[i, j] = max(max_lens[i - 1, j], max_lens[i, j - 1], max_lens[i - 1, j - 1] + 1)
            else:
                max_lens[i, j] = max(max_lens[i - 1, j], max_lens[i, j - 1], max_lens[i - 1, j - 1])
    return a, b, max_lens[m - 1, n - 1]


def get_max_inc_sub(arr):
    n = len(arr)
    last_num, length = 0, 0
    states = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if arr[i] > last_num:
                states[i, length]

# 这TM就是棋盘那题嘛
MAX_WEIGHT = 10
def length_of_yanghui(arr_tree, i, l):
    count = len(arr_tree)
    levels = int(math.log2(1 + count))
    states = np.zeros((count, MAX_WEIGHT))
    weights = np.ones((count, MAX_WEIGHT))
    # print(states)
    # print(arr_tree[list(range(2 ** i - 1, 2 ** (i + 1) - 1))])
    # for i in range(0, levels):
    #     for j in range(2 ** i - 1, 2 ** (i + 1) - 1):


if __name__ == '__main__':
    # arr = np.random.randint(1, MAX_WEIGHT, size=(10, 10), dtype='i')
    # print(arr)
    # print(length_of_yanghui(arr, 3, 1))
    # np.array([i ** 1 for i in range(125)]

    a = 'astsfatmu'
    b = 'asbfsatq'
    print(get_levens_dis_retro(a, b))

    a = 'astsfatmuqtppppaaaaajjj'
    b = 'asbfsatqspdspttttppppppppppbpjjjppcpt'
    # print(get_levens_dis_retro(a, b))  # 没错啊，最小编辑距离还是5啊，你人肉做一次看看。别以为加个字母就会有啥影响，人家可是遍历了整个空间求出的最小值

    # print(get_max_shared_substr_retro(a, b))
    print(get_max_shared_substr_dp(a, b))

    a = 'abcdef'
    b = 'ace'
    print(get_max_shared_substr_dp(a, b, True))