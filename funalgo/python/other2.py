from collections import deque


def next_greater_element(arr):
    win = deque()
    res = [-1] * len(arr)
    for i in reversed(range(len(arr))):
        while win and arr[i] >= win[0]:
            win.popleft()
        res[i] = win[0] if win else -1
        win.appendleft(arr[i])
    return res


def next_greater_element_in_loop(arr):
    win = deque()
    res = [0] * len(arr)
    for i in reversed(range(2 * len(arr))):
        ni = (i - len(arr)) % len(arr)
        while win and arr[ni] >= win[0]:
            win.popleft()
        if res[ni] == 0 or res[ni] == -1:
            res[ni] = win[0] if win else -1
        win.appendleft(arr[ni])
    return res


def wait_for_next_warmer_day(arr):
    win = deque()
    res = [-1] * len(arr)
    for i in reversed(range(len(arr))):
        # while win and arr[i] >= win[0][0]:
        #     win.popleft()
        # res[i] = win[0][1] - i if win else -1
        # win.appendleft((arr[i], i))
        while win and arr[i] >= arr[win[0]]:
            win.popleft()
        res[i] = win[0] - i if win else -1
        win.appendleft(i)
    return res


def findTargetSumWays1(nums: list, S: int) -> int:
    queue = []
    res = 0

    def trace_back(i, acc, target):
        if i >= len(nums):
            if acc == target:
                nonlocal res
                res += 1
            return
        # queue.append(num)
        trace_back(i + 1, acc + nums[i], target)
        # queue.pop()
        # queue.append(-num)
        trace_back(i + 1, acc - nums[i], target)
        # queue.pop()

    trace_back(0, 0, S)
    return res


def findTargetSumWays2(nums: list, S: int) -> int:
    demo = {}

    def dp(i, rest):
        if i >= len(nums):
            return 1 if rest == 0 else 0  # 别忘了判断rest==0！
        if (i, rest) in demo:
            return demo[(i, rest)]
        else:
            foward_meth_count = dp(i + 1, rest - nums[i]) \
                                + dp(i + 1, rest + nums[i])
            return foward_meth_count

    return dp(0, S)
    # return demo[(len(nums) - 1, S)]


def primary_bag_problem2(values, weights, W):
    assert len(values) == len(weights)
    N = len(values)
    # dp = [[0] * (W + 1) for i in range(N)]
    # 都+1就统一了。完美
    dp = [[0] * (W + 1) for i in range(N + 1)]
    # 这个base case感觉不是很美，可不可以再打磨一下？
    # dp[0][weights[0]] = values[0]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            selected = dp[i - 1][j - weights[i - 1]] + values[i - 1] \
                if j - weights[i - 1] >= 0 else 0
            not_selected = dp[i - 1][j]
            dp[i][j] = max(selected, not_selected)
    return dp[N][W]


def primary_bag_problem1(values, weights, W):
    assert len(values) == len(weights)
    N = len(values)
    demo = {}

    def dp(i, rest, value):
        if (i, rest) in demo:
            return demo[(i, rest)]
        res = None
        if i >= N:
            res = value if rest >= 0 else 0
        else:
            # if rest - weights[i] > 0:
            res = max(dp(i + 1, rest - weights[i], value + values[i]),
                      dp(i + 1, rest, value))
        demo[(i, rest)] = res
        return res
        # else:
        #     return dp(i + 1, rest, value + values[i])

    return dp(0, W, 0)


def subset_summation(arr) -> bool:
    _sum = sum(arr)
    if _sum % 2 != 0: return False  # !!
    _sum //= 2
    # dp = [[False] * (_sum + 1) for i in range(len(arr) + 1)]
    dp = [False] * (_sum + 1)
    # for i in range(len(dp)):
    #     dp[i][0] = True
    dp[0] = True
    # for i in range(1, len(dp)):
    for i in range(1, len(arr) + 1):
        for j in range(1, _sum + 1):
            # for j in range(1, _sum // 2 + 1):
            if j - arr[i - 1] >= 0:
                # dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                dp[j] = dp[j - arr[i - 1]] or dp[j]
            # else:
                # dp[i][j] = False
                # 当前状态下肯定装不下，寄希望于"前面的状态 没装i 的结果了"
                # dp[i][j] = dp[i - 1][j]
    # return dp[len(arr)][_sum]
    return dp[_sum]


if __name__ == '__main__':
    print(next_greater_element([2, 1, 2, 4, 3]))
    print(wait_for_next_warmer_day([73, 74, 75, 71, 69, 72, 76, 73]))
    print(next_greater_element_in_loop([2, 1, 2, 4, 3]))
    print(findTargetSumWays2([1, 1, 1, 1, 1], 3))

    print(primary_bag_problem1([4, 2, 3], weights=[2, 1, 3], W=4))
    print(primary_bag_problem2([4, 2, 3, 5], weights=[2, 1, 3, 2], W=4))
    print(subset_summation([1, 2, 3, 5]))
    print(subset_summation([1, 2, 3, 1, 2, 3, 4, 3, 3]))
