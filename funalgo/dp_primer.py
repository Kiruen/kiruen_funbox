import numpy as np
import math
import numpy as np
from functools import lru_cache

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


def get_levens_dis(a, b, i, j, edit):
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
    arr = np.random.randint(1, MAX_WEIGHT, size=(10, 10), dtype='i')
    print(arr)
    print(length_of_yanghui(arr, 3, 1))
    # np.array([i ** 1 for i in range(125)]
