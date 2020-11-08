import functools
import numpy as np
import copy
import os, sys


def reverse(arr, end) -> list:
    reversed_arr = [arr[end]]
    if end == 0:
        return reversed_arr
    else:
        reversed_arr.extend(reverse(arr, end - 1))
        return reversed_arr


def insert_sort(arr, end) -> list:
    if end == 0:
        return arr[:1]
    isorted = insert_sort(arr, end - 1)
    for i in range(len(isorted) + 1):
        # if i == len(isorted):
        #     isorted.append(arr[end])
        if i == len(isorted) or arr[end] < isorted[i]:
            isorted.insert(i, arr[end])
            break
    return isorted


def print_i_to_j(arr, i, j, cur=0):
    if i <= cur <= j:
        print(arr[cur], end=' ')
    if cur <= j:
        print_i_to_j(arr, i, j, cur + 1)


def find_minimum_of_rotate_arr(rotate_arr, l=0, r=-1):
    if r == -1: r = len(rotate_arr) - 1
    mid = (l + r) // 2
    mid_n = rotate_arr[mid]
    left_n, right_n = rotate_arr[l], rotate_arr[r]
    if l == r - 1:
        return min(left_n, right_n)
    if left_n == mid_n == right_n:
        return min(rotate_arr)  # 该策略无效，改用朴素策略
    if mid_n >= left_n:  # 表明左边有序
        return find_minimum_of_rotate_arr(rotate_arr, mid, r)  # 不管怎么样，把mid包括进来不会错的！
    else:
        return find_minimum_of_rotate_arr(rotate_arr, l, mid)


@functools.lru_cache(maxsize=1024)
def climb_stairs(steps: tuple, n) -> int:
    if n == 0 or n == 1: return 1  # n == 0也应该是1种情况啊，类似排列组合数C(0,n)
    strategies = 0
    for step in steps:
        if n - step >= 0:
            strategies += climb_stairs(steps, n - step)
    return strategies


def find_target_str(strs, target) -> int:
    '''
    :param strs:有序的插空字符串数组
    '''
    l, r = 0, len(strs) - 1
    while l <= r:
        mid = (l + r) // 2
        while mid > l and strs[mid] == "":
            mid -= 1
        # while mid < r and strs[mid] == "":
        #     mid += 1
        if strs[mid] == target:
            return mid
        elif strs[mid] < target:  # 在右边
            l = mid + 1
        else:
            r = mid - 1
        print(l, mid, r)


def pow(n, e):
    i, res = 1, 1
    temp_res, temp_e = n, e  # i=1 res=n   i=2 res=n^2
    if e == 1: return res
    while temp_e > 0:
        while (i << 1) < temp_e:
            i <<= 1
            temp_res *= temp_res
        if i <= temp_e:  # 检查一下成果：如果你积累够了，就给res加点油，然后准备下一轮
            res *= temp_res
            temp_res = n
        temp_e -= i
        i = 1
    return res
    # while i < e:
    #     i += 1
    #     res *= n
    # return res * pow(n, e - i)


def get_legal_brackets(n):
    results = set()
    results.add("()")
    if n > 1:
        for i in range(n - 1):
            new_results = set()  # 由于下一级不会使用上一级的结果，只会修改，因此不需要深拷贝results（下面的求自己问题就不是这样的了）
            for res in results:
                new_results.add(f"{res}()")
                new_results.add(f"(){res}")
                new_results.add(f"({res})")
            results = new_results
    return results


def gen_subset(s):
    # 递归版本
    def gen_subset_recur(s: list, i_to_select, temp, subs):
        if i_to_select >= len(s):
            subs.append(temp.copy())
            return
        # print(temp, s[i_to_select])
        has_temp = temp.copy()
        has_temp.append(s[i_to_select])
        gen_subset_recur(s, i_to_select + 1, has_temp, subs)

        not_has_temp = temp.copy()
        # print(temp)
        gen_subset_recur(s, i_to_select + 1, not_has_temp, subs)

    # 迭代版本
    def gen_subset_iter(s):
        g_temps = [[]]  # 允许元素重复，所以用list更好
        for i, e in enumerate(s):
            new_temps = g_temps.copy()
            for old_temp in new_temps:
                new_temp = old_temp.copy()
                new_temp.append(e)
                g_temps.append(new_temp)
            # g_temps = new_temps  # 这句就不要了啊，否则就会无休止循环。python的迭代器和c#的不一样啊
        return g_temps

    # 二进制模型版本
    def gen_subset_binary(s):
        subs = []
        num_max = pow(2, len(s)) - 1
        s = list(sorted(s))
        for i in range(pow(2, len(s))):  # 可配合maxnum---，以产生一个字典序顺序的列表。这是字典序吗？？
            num = num_max - i
            sub = []
            for k in range(0, len(s)):
                if (num >> (len(s) - 1 - k)) & 1 == 1:
                    sub.append(s[k])
            subs.append(sub)
        return subs

    res = []
    # gen_subset_recur(s, 0, [], res)
    res = gen_subset_binary(s)
    return res


def clear_rows_and_cols_with_zero(matrix):
    # zero_indexes = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 0]
    # i_set, j_set = set((i for i, _ in zero_indexes)), set((j for _, j in zero_indexes))
    i_set, j_set = np.zeros(len(matrix), dtype='i'), np.zeros(len(matrix[0]), dtype='i')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                i_set[i] = True
                j_set[j] = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i_set[i] or j_set[j]:
                # if i in i_set or j in j_set:
                matrix[i][j] = 0


def get_most_votes(states, time):
    # 递归+备忘录版本
    @functools.lru_cache(maxsize=32)
    def get_most_votes_recur(i_todeter, time):
        if time <= 0 or i_todeter >= len(states):
            return 0
        ifpresent = states[i_todeter]['votes'] + get_most_votes_recur(i_todeter + 1, time - states[i_todeter]['time'])
        ifabsent = get_most_votes_recur(i_todeter + 1, time)
        return max(ifpresent, ifabsent)

    # 迭代/DP版本
    def get_most_votes_iter(time):
        g_max = -1
        time_types = time + 1
        dp = np.zeros(len(states) * time_types, dtype='i')
        dp.shape = (len(states), time_types)
        for _state in range(dp.shape[0]):
            dp[_state][0] = 0
            dp[_state][1] = states[_state]['votes'] if states[_state]['time'] <= 1 else 0
        for _time in range(dp.shape[1]):
            dp[0][_time] = 0
            dp[1][_time] = states[1]['votes'] if states[1]['time'] <= _time else 0

        # for _state in range(len(states)):
        #     for _time in range(time_types):
        for _time in range(time_types):
            for _state in range(len(states)):
                if _time >= states[_state]['time']:
                    # 转移的起点是dp[i-1]！别搞错了。
                    local_max = max(dp[_state - 1][_time],
                                    dp[_state - 1][_time - states[_state]['time']] + states[_state]['votes'])
                    dp[_state][_time] = local_max
                    if g_max < local_max:
                        g_max = local_max
                else:
                    dp[_state][_time] = dp[_state - 1][_time]
        return g_max

    return get_most_votes_iter(time)
    # return get_most_votes_recur(0, time)


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(reverse(arr, len(arr) - 1))

    arr = [3, 1, 5, 2]
    print(insert_sort(arr, len(arr) - 1))
    print_i_to_j(arr, 1, 2)
    print()

    print(climb_stairs((1, 2, 3), 5))
    print(climb_stairs((1, 2, 4, 5), 200))

    print(find_minimum_of_rotate_arr([4, 5, 1, 2, 3]))
    print(find_minimum_of_rotate_arr([5, 6, 7, 8, 2, 2, 3, 4]))

    print(find_target_str(["a", "", "b", "", "", "", "c"], "a"))
    print(pow(2, 15))

    arr = [[1, 2, 0, 4, 5],
           [1, 0, 1, 4, 5],
           [1, 2, 1, 4, 8],
           [1, 2, 0, 5, 6], ]
    clear_rows_and_cols_with_zero(arr)
    print(arr)

    for i in range(1, 6):
        print(get_legal_brackets(i))

    res = gen_subset([1, 2, 3])
    print(len(res), res)

    all_states = [
        {'name': '加利福尼亚州', 'votes': 55, 'time': 5},
        {'name': '德克萨斯州', 'votes': 38, 'time': 3},
        {'name': '佛罗里达州', 'votes': 29, 'time': 2},
        {'name': '纽约州', 'votes': 29, 'time': 2},
        {'name': '伊利诺伊州', 'votes': 20, 'time': 1},
        {'name': '宾西法利亚州', 'votes': 20, 'time': 1},
        {'name': '俄亥俄州', 'votes': 18, 'time': 1},
        {'name': '密歇根州', 'votes': 16, 'time': 1},
        {'name': '乔治亚州', 'votes': 16, 'time': 1},
        {'name': '北卡罗来纳州', 'votes': 15, 'time': 1}
    ]
    print(get_most_votes(all_states, 10))
    # print("" < "1" < "12" < "3")