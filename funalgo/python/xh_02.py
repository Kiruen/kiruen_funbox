from collections import deque


def get_window_max(arr, win_size):
    queue = deque()
    res = []
    # i, j = 0, 0
    # while i < len(arr) and j < len(arr):
    for j in range(len(arr)):
        while len(queue) > 0 and queue[-1] < arr[j]:
            queue.pop()

        queue.append(arr[j])

        # 如果队头恰好是即将抹去的左边界，那么即使它再大，我们也要舍弃它了
        if j >= win_size and len(queue) > 0 \
                and queue[0] == arr[j - win_size]:
            queue.popleft()
        # if j - i + 1 >= win_size:
        if j >= win_size - 1:
            res.append(queue[0])
        j += 1
    return res


def get_len_of_longest_no_repeat(txt):
    # win = set()
    win = {}  # 字符→位置.next的dict！因为窗口内肯定不会有重复，所以天然适合用dict
    left, right = 0, 0
    len_result, range_result = 0, None
    while left < len(txt) and right < len(txt):
        ncur = txt[right]
        if ncur in win:
            # left = win[ncur]
            # 害，这句其实是因为以前的old可能没remove掉。你完全可以remove掉嘛。
            # 不过你也要注意，应该把捣蛋鬼之前的元素全部remove掉！
            left = max(win[ncur], left)  #只有win[ncur]在当前窗口内，我们才视它为捣蛋鬼，否则无视它！
            # left = win[ncur]
            # win.pop(ncur)
        win[ncur] = right + 1  # .next!直接跳了

        if len_result < right - left + 1:
            len_result = right - left + 1
            range_result = (left, right)

        right += 1
        # if txt[right] not in win:
        #     # win.add(txt[right])
        #     win[txt[right]] = right
        #     right += 1
        #     result = max(result, right - left)
        # else:
        #     # nrepeat = txt[right]
        #     # while txt[left] != nrepeat:
        #     #     # 注意是左边界+1！
        #     #     left += 1
        #     left = win.pop(txt[right]) + 1

    return len_result, txt[range_result[0]:range_result[1] + 1]


def get_len_of_longest_no_repeat2(txt):
    map = [-1] * 256
    left, right = 0, 0
    res = 0
    while left < len(txt) and right < len(txt):
        chcur = txt[right]
        iascii = ord(chcur)
        # if map[iascii] != -1:
        left = max(left, map[iascii])
        map[iascii] = right + 1
        res = max(res, right - left + 1)
        right += 1
    return res

def find_anagrams(str_main, str_pattern):
    def is_same_with_pattern(arr1, arr2):
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True

    a_code = ord('a')
    sArr = [0] * 26
    pArr = [1 if chr(a_code + i) in str_pattern else 0 for i in range(0, 26)]
    res = []
    left, right = 0, 0
    while left < len(str_main) and right < len(str_main):
        sArr[ord(str_main[right]) - a_code] += 1
        if right > len(str_pattern) - 1:
            sArr[ord(str_main[left]) - a_code] -= 1
            left += 1
        if right >= len(str_pattern) - 1 and\
            is_same_with_pattern(sArr, pArr):
            res.append(left)
        right += 1
    return res


if __name__ == '__main__':
    print(get_len_of_longest_no_repeat("ababcabdefkt1fasf2345"))
    print(get_len_of_longest_no_repeat2("ababcabdefkt1fasf2345"))
    print(get_window_max([1, 2, 1, 6, 5, 3, 8, 1, 9, 1, 1, 1, 1], 4))
    print(find_anagrams("atdatasasatd", "adt"))