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


def findTargetSumWays(nums: list, S: int) -> int:
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


if __name__ == '__main__':
    print(next_greater_element([2, 1, 2, 4, 3]))
    print(wait_for_next_warmer_day([73, 74, 75, 71, 69, 72, 76, 73]))
    print(next_greater_element_in_loop([2, 1, 2, 4, 3]))
    print(findTargetSumWays([1,1,1,1,1], 3))