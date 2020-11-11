from collections import deque

def collect_max_in_windows(arr, win_size):
    queue_max = deque()
    res = []
    # left, right = 0, 0 不一定要显式定义l r
    for i, n in enumerate(arr):
        while len(queue_max) > 0 and arr[queue_max[-1]] <= n:
            queue_max.pop()
        queue_max.append(i)
        if i - win_size >= queue_max[0]:
            queue_max.popleft()
        # left += 1
        # right += 1
        if i + 1 - win_size >= 0:  # 窗口左边界超过了0，完整的窗口出现了！
            res.append(arr[queue_max[0]])
    return res


def count_of_delta_of_subarray(arr, delta_aim):
    max_deque = deque()
    min_deque = deque()
    res = 0
    L, R = 0, 0
    while L < len(arr):
        while R < len(arr):
            while len(min_deque) > 0 and arr[min_deque[-1]] >= arr[R]:
                min_deque.pop()
            min_deque.append(R)
            while len(max_deque) > 0 and arr[max_deque[-1]] <= arr[R]:
                max_deque.pop()
            max_deque.append(R)

            if L > min_deque[0]:
                min_deque.popleft()
            if L > max_deque[0]:
                max_deque.popleft()
            if arr[max_deque[0]] - arr[min_deque[0]] >= delta_aim:
                res += R - L + 1
                break
            R += 1
        L += 1
    return res


def collect_most_nearby_max_both_side_foreach(arr):
    import numpy
    stack = deque()
    res = list([None, None] for i in range(len(arr)))
    # res = [None, None] * len(arr)
    # res = numpy.arange(2 * len(arr))
    # res.shape = (len(arr), 2)
    for i, n in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] < n:
            e = stack.pop()
            res[e][0] = arr[stack[-1]] if len(stack) > 0 else None
            res[e][1] = n
        stack.append(i)
    while len(stack) > 0:
        e = stack.pop()
        res[e][0] = arr[stack[-1]] if len(stack) > 0 else None
    return res


if __name__ == '__main__':
    print(collect_max_in_windows([5,4,1,3,6,7,1,2,3], 3))
    print(count_of_delta_of_subarray([3,1,4,2,5], 2))
    print(collect_most_nearby_max_both_side_foreach([1,7,6,8,4,2]))