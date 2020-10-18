import collections as coll
import sys

# 求正序最大相邻两数数字差
def get_max_gap(arr):
    _min, _max, ncount = min(arr), max(arr), len(arr)
    def get_bid(num):  # 0 1 2 3 4
        bid = (num - _min) * ncount // (_max - _min)
        # print(bid)
        return bid
    # bucket_factory = coll.namedtuple('Bucket', ['max', 'min', ''])
    bucks = [[False, sys.maxsize, -sys.maxsize] for i in range(ncount + 1)]
    bucks[0], bucks[ncount] = [False, _min, _min], [False, _max, _max]
    for num in arr:
        bid = get_bid(num)
        bucks[bid][1] = min(num, bucks[bid][1])
        bucks[bid][2] = max(num, bucks[bid][2])
        bucks[bid][0] = True
    max_gap, i_last_nempty = 0, 0
    for i in range(ncount + 1):
        if bucks[i][0] is True:
            max_gap = max(max_gap, bucks[i][1] - bucks[i_last_nempty][2])
            i_last_nempty = i

    return max_gap, bucks

if __name__ == '__main__':
    print(get_max_gap([7,4,1,8,11]))
    print(type(10 ** 100))
