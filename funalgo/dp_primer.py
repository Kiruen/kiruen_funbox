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
    """TODO:把最长公共子序列在原数组中标记出来"""
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
    """返回序列中最长的增序子序列，比如2, 9, 3, 6,5, 1, 7这样一组数字序列，
    它的最长递增子序列就是2, 3, 5, 7，所以最长递增子序列的长度是4
    """
    n = len(arr)
    last_num, length = 0, 0
    states = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if arr[i] > last_num:
                states[i, length]

# @lru_cache(maxsize=4096)
# lru_cache底层维护了一个：[arg_tuple]→[value]的映射，但是访问不到啊，只能求个方案数量，但不知道方案具体是啥啊
scheme_que = []
schemes = []
def get_coin_scheme_types_memo(coins: tuple, i: int, total: int, verbose :bool=False) -> int:
    """
    给定金币面值和总金额，找出有多少凑整方案（使用回溯+备忘录）
    思路：面额逆序排序，从左边开始试，每个面额尝试不同的个数，再加上
    """
    res = False  # 指示该方案是否能正好凑足整
    if total == 0:
        # sys.stdout.write(f'{schemes}')
        schemes.append(scheme_que)
        if verbose:
            print(scheme_que)
        res = True
    else:
        if i == len(coins):
            res = total == 0
        else:
            count = 0
            coin = coins[i]
            while count * coin <= total:  # 有个增强画面感的技巧：假如此时在试中间那个金币，你想象向后面扔回旋镖，回旋镖回来时带个OK/NO，再一次向后扔
                if count > 0:
                    scheme_que.append((coin, count))

                isok = get_coin_scheme_types_memo(coins, i + 1, total - coin * count)  # OK向上冒泡，传播方案合格的消息
                res += isok

                if count > 0:
                    scheme_que.pop()
                count += 1
    return res


def get_fewest_coin_scheme_dp(coins: list, i: int, total: int) -> int:
    """
    给定金币面值和总金额，找出金币数最少的方案（使用dp）
    """
    pass


def fewest_coin_count_memo(coins: list, index: int, total: int) -> int:
    """
    给定金币面值和总金额，找出金币数最少的组合（使用回溯+备忘录）
    """
    max_steps = total // min(coins)
    states = np.zeros((total, len(coins)), dtype='i')
    for i in range(max_steps):
        for j in range(total):
            pass

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

    # 2,3,5,7,11,13
    scheme_count = get_coin_scheme_types_memo((13, 11, 7, 5, 3, 2), 0, 200)
    print(scheme_count, len(schemes) == scheme_count)