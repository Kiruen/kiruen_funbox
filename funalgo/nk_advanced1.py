import copy


# 求next数组
def get_next(arr):
    _next = [-1] * len(arr)
    print(_next)
    _next[1] = 0
    i, sta = 2, _next[2 - 1]
    while i < len(arr):
        if arr[sta] == arr[i - 1]:  # 要求next[i]，又想偷懒，肯定只能依赖0~i-1子串咯
            sta += 1
            _next[i] = sta
            i += 1
        elif _next[sta] > 0:  # != -1 和0
            sta = _next[sta]
        else:
            _next[i] = 0
            i += 1
    return _next


class BTree(object):

    # 初始化
    def __init__(self, data, left=None, right=None):
        self.data = data  # 数据域
        self.left = left.copy() if left else None  # 左子树
        self.right = right.copy() if right else None  # 右子树
        # self.dot = Digraph(comment='Binary Tree')

    def copy(self):
        return BTree(1, self.left.copy() if self.left else None,
                     self.right.copy() if self.right else None, )

    def graph(self, level=0):
        text = "{}{}\n".format("\t" * level, self.data)
        text += self.left.graph(level + 1) if self.left else "{}#\n".format("\t" * (level + 1))
        text += self.right.graph(level + 1) if self.right else "{}#\n".format("\t" * (level + 1))
        return text

    def serilize(self):
        """二叉树的序列化(扁平化)，实质是补全/满二叉化。
        这样能唯一表示一颗二叉树，且先序(中后都行)遍历就能还原(反序列化)回来
        """
        text = "{}_{}{}".format(self.data,
                                self.left.serilize() if self.left else "#_",
                                self.right.serilize() if self.right else "#_")
        return text

    def __repr__(self):
        return self.graph()


def bta_has_btb(bta: BTree, btb: BTree):
    return bta.serilize().find(btb.serilize()) != -1


def is_patterned():
    """
    判断字符串是否是由某个模式串重复得到的
    """
    pass


def get_top_k(arr, top, l=0, r=-1):
    """返回序列中的第K大数，要求时间复杂度O(N)"""
    if r == -1: r = len(arr) - 1  # 两边的区域：[l, left] [right, r]，这个区间的开闭一定要明确，否则边界抠不好
    if l >= r:
        return arr[l]

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    pivot = arr[l]
    left, right = l - 1, r + 1
    i = l
    while left < right and i < right:  # 出现诡异的错误。。一定要第一时间调试，不要干想
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            left += 1
            swap(arr, i, left)  # 扩充区域，肯定是把区域【之外】的数挪一下腾地方
        else:
            right -= 1
            swap(arr, i, right)
    print(arr)
    if left >= top:
        return get_top_k(arr, top, l, left)
    elif left < top < right:
        return arr[top]
    elif top >= right:
        return get_top_k(arr, top, right, r)


def BFPRT(arr, ):

    pass


if __name__ == '__main__':
    print(get_next('ababac'))

    bt1 = BTree(1)
    bt2 = BTree(1, bt1, bt1)
    bt3 = BTree(1, bt1)
    bt4 = BTree(1, bt2, bt3)
    print(bt2.left is bt1)

    print(bt4.serilize())

    print(bta_has_btb(bt2, bt1))
    print(bta_has_btb(BTree(1, bt2), BTree(1, bt1)))


    print(get_top_k([1, 4, 4, 1, 5, 5], 4))
    # print(get_top_k([1, 4, 2, 8, 3, 2, 7, 9], 4))
