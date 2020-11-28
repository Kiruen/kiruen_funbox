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


if __name__ == '__main__':
    print(trans_min([1, 3, 5, 6, 7, 8, 9], 4))  # sorted([1,3,2,7,4,6])
    print(trans_min(list(range(1, 11)), 5))
