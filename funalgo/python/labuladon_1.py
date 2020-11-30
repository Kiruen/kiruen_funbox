def open_lock(deadends, target):
    visited = set(deadends)
    qs, ts = set(), set()
    while True:
        pass


def trans_min(weights: list, day_limit: int):
    def can_finish(cap: int):
        i = 0
        for d in range(day_limit):
            remaining_cap = cap
            # 尝试装入下一个货物，装不下就等明天
            while (remaining_cap - weights[i]) >= 0:
                remaining_cap -= weights[i]
                i += 1
                if i >= len(weights):
                    return True
        return False

    left, right = max(weights), sum(weights) + 1
    while left < right:  # 在left == right 的时候正好停止
        mid = left + (right - left) // 2  # 其实多此一举了，因为python不会溢出
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    return left


def coin_change(coins: list, target: int):
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[target] if dp[target] <= len(coins) else -1


def max_ascending_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(len(dp)):
        # cur_max_len = -1
        for j in range(i):  # i + 1
            if arr[j] < arr[i]:
                # cur_max_len = max(cur_max_len, dp[j] + 1)
                dp[i] = max(dp[i], dp[j] + 1)
        # dp[i] = cur_max_len  # 不能到这里才把max赋给dp，因为dp[0]会被搞成-1
    return max(dp)


def max_common_subsequence_bf(str1, str2):
    def dp(i, j):
        if i == -1 or j == -1: return 0
        if str1[i] == str2[j]:
            return dp(i - 1, j - 1) + 1
        else:
            return max(dp(i - 1, j), dp(i, j - 1))

    return dp(len(str1) - 1, len(str2) - 1)


def max_common_subsequence_dp(str1, str2):
    dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]


def guess_egg_hardness(max_floor, egg_limit):
    memo = dict()

    # 写这种内嵌函数要小心，不要把外层的参数和内层的参数搞混
    def dp(floor, egg):
        if (floor, egg) in memo:
            return memo[(floor, egg)]
        if floor <= 0:
            return 0
        elif egg == 1:
            return floor  # 这也体现出最坏情况！
        min_time = floor + 1
        l, r = 1, floor  # 注意l从1开始
        while l <= r:
            mid = (r + l) // 2
            broken = dp(mid - 1, egg - 1)  # 摔坏的情况下，我们要尝试的次数
            not_broken = dp(floor - mid, egg) # 没摔坏的情况下，我们要尝试的次数
            if broken > not_broken:  # 应该向楼下搜索，因为次数更多
                r = mid - 1
                min_time = min(broken + 1, min_time)
            else:
                l = mid + 1
                # 都要+1，因为都扔了一次啊。本质上是吧max分成两个if了。
                min_time = min(not_broken + 1, min_time)
        # for k in range(1, floor + 1):
        #     # 在k处摔坏了，然后从一个一个往上试
        #     # min_time = min(dp(k, j) + j - k, min_time)
        #     # 如果摔坏了、如果没摔坏
        #     min_time = min(min_time,
        #                    max(dp(k - 1, egg - 1), dp(floor - k, egg)) + 1)
        memo[(floor, egg)] = min_time
        return min_time

    return dp(max_floor, egg_limit)


if __name__ == '__main__':
    print(trans_min([1, 3, 5, 6, 7, 8, 9], 4))  # sorted([1,3,2,7,4,6])
    print(trans_min(list(range(1, 11)), 5))
    print(coin_change([1, 2, 5], 3))
    print(coin_change([1, 1, 1, 3], 3))
    print(coin_change([2, 4, 1, 5], 8))
    # assert coin_change([1,2,5], 3) == 2
    print(max_ascending_subsequence([1, 4, 3, 4, 2, 3]))

    print(max_common_subsequence_bf("aced", "abcded"),
          max_common_subsequence_dp("aced", "abcded"))
    print(max_common_subsequence_dp("acede", "abcdedaae"))
    print()
    print(guess_egg_hardness(100, 2))
