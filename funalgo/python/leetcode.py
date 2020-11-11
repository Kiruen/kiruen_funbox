import math
import sys


def clamp(n, l=0, r=sys.maxsize):
    return max(min(n, r), l)


def get_longest_succ_subarray(arr):
    longest = []
    i, j = 0, 0
    while i < len(arr) and j < len(arr):
        if j == len(arr) - 1 or arr[j] > arr[j + 1]:
            if len(longest) < j + 1 - i:  # 加等号就输出最后一个最长的（长度相等的情况下）
                longest = arr[i:j + 1]
            i = j = j + 1
        else:
            j += 1
    return longest


def get_max_profit1(_prices):
    def double_pointer_algo(prices):
        i, j = 0, 0
        profit = 0
        while i < len(prices) and j < len(prices):
            if j == len(prices) - 1 or prices[j] > prices[j + 1]:
                # 该卖了
                profit += prices[j] - prices[i]
                i = j = j + 1
            else:
                j += 1
        return profit

    def dp_algo(prices):
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]  # 0卖1买
        for i in range(1, len(prices)):
            # 今天想卖：有可能昨天卖了，没得卖了，沿用昨天的总收益；也可能是昨天买了，今天正好卖，收益++
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 今天想买：有可能昨天买了，今天不能再买，沿用昨天的总收益；也可能是昨天刚卖过，今天又买入，收益暂时--
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        # 最大收益显然是：最后一天仍然在卖 的情况下产生？。不确定可以加个max。
        # 破案了，是因为最后一天不允许买，即使产生了最大收益也是非法的
        return dp[len(prices) - 1][0]  # max(dp[len(prices) - 1][0], dp[len(prices) - 1][1])

    return double_pointer_algo(_prices), dp_algo(_prices)


def get_parts_of_target(arr, target):
    res = []
    if len(arr) < 1123:
        filter = [-1] * target
        for i, n in enumerate(arr):
            if n < target:
                filter[n] = i
        for n in arr:
            # if filter[clamp(target - n, 0)] == 1:  # 用clamp大错特错
            if 0 <= target - n <= len(filter) and filter[target - n] != -1:
                res.append({filter[target - n]:target - n, filter[n]:n})
                # 防止重复
                filter[target - n] = filter[n] = -1
    else:
        # s = frozenset(arr)
        m = {n: i for i, n in enumerate(arr)}
        for n in arr:
            if m.get(target - n, -1) != -1 and m.get(n, -1) != -1:
                res.append({m[target - n]:target - n, m[n]:n})
                m[n] = m[target - n] = -1
                # s.remove(target - n)
                # s.remove(n)
    return res


if __name__ == '__main__':
    print(get_max_profit1([1, 5, 4, 3, 6, 1]))
    print(get_longest_succ_subarray([1, 3, 2, 5, 6, 1, 7, 8, 9, 1]))
    print(get_longest_succ_subarray([1, 3, 2, 4, 1]))

    print(get_max_profit1([7, 1, 5, 3, 6, 4]))
    print(get_max_profit1([1, 2, 3, 4, 5, 1]))
    print(get_parts_of_target([1, 2, 4, 5], 6))
