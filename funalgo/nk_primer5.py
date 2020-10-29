from collections import deque


class BTreeSerializationMixin():
    def __init__(self):
        self.visited = [False, False]

    def set(self, node, lr='l'):
        if node and node.is_empty():
            node = None
        if lr == 'l':
            self.left = node
            self.visited[0] = True
        elif lr == 'r':
            self.right = node
            self.visited[1] = True
        else:
            raise Exception("wrong index")

    def has_visited(self, lr='l'):
        if lr == 'l':
            return self.visited[0]
        elif lr == 'r':
            return self.visited[1]
        else:
            raise Exception("wrong index")

    @staticmethod
    def deserialize(code: str):
        queue = deque()
        node_strs = code.split('_')
        cur_node, new_node = BTree(node_strs[0]), None
        root = cur_node
        queue.append(root)
        for node_str in node_strs[1:-1]:
            # print(list(map(lambda x: x.data, queue)), node_str)
            new_node = BTree(node_str)  # if node_str != '#' else None

            if not cur_node.left or not cur_node.has_visited('l'):
                cur_node.set(new_node, 'l')
            elif not cur_node.right or not cur_node.has_visited('r'):
                cur_node.set(new_node, 'r')

            if not new_node.is_empty():
                queue.append(new_node)
                cur_node = new_node
            elif len(queue) > 0:
                cur_node = queue.pop()
                print(cur_node.data)
        return root

    def deserialize_level(self):
        return 1

    @staticmethod
    def deserialize_recur(code: str):
        queue = deque()
        node_strs = code.split('_')
        for node_str in node_strs:
            queue.append(node_str)

        def consume():
            cur = queue.popleft()
            if cur == '#':
                return None
            node = BTree(cur)
            node.left = consume()
            node.right = consume()
            return node

        return consume()


class BTree(BTreeSerializationMixin):
    # 初始化
    def __init__(self, data, left=None, right=None):
        BTreeSerializationMixin.__init__(self)
        self.data = data  # 数据域
        self.left = left.copy() if left else None  # 左子树
        self.right = right.copy() if right else None  # 右子树

    def copy(self):
        return BTree(self.data, self.left.copy() if self.left else None,
                     self.right.copy() if self.right else None, )

    def graph(self, level=0):
        text = ""
        text += self.right.graph(level + 1) if self.right else "{}#\n".format("\t" * (level + 1))
        text += "{}{}\n".format("\t" * level, self.data)
        text += self.left.graph(level + 1) if self.left else "{}#\n".format("\t" * (level + 1))
        return text

    def serialize(self):
        """二叉树的序列化(扁平化)，实质是补全/满二叉化。
        这样能唯一表示一颗二叉树，且先序(中后都行)遍历就能还原(反序列化)回来
        """
        text = "{}_{}{}".format(self.data,
                                self.left.serialize() if self.left else "#_",
                                self.right.serialize() if self.right else "#_")
        return text

    def is_empty(self):
        return self.data == '#'

    def __repr__(self):
        return self.graph()

    @classmethod
    def is_bsearch(cls, node):
        if node.left and node.right:
            return int(node.left.data) <= node.data < int(node.right.data) \
                   and BTree.is_bsearch(node.left) and BTree.is_bsearch(node.right)
        elif node.left:
            return BTree.is_bsearch(node.left)
        elif node.right:
            return BTree.is_bsearch(node.right)
        else:
            return True

    @classmethod
    def is_complete(cls, node):
        if node.left and node.right:
            return BTree.is_complete(node.left) and BTree.is_complete(node.right)
        elif not node.left and node.right:
            return False
        elif not node.right and node.left:
            return node.left.left is None
        else:
            return True

    def count(self):
        return BTree.count_of_node(self, 0, BTree.left_most_level(self, 0))

    @staticmethod
    def count_of_node(node, level, max_level):
        '''
        :param level:目前节点所属层次
        :param max_level:最左下的层次
        '''
        if level == max_level:
            return 1  # 到叶子了，叶子子树的结点数当然=1
        # left_level = BTree.left_most_level(parent.left, level)
        # right_level = BTree.left_most_level(parent.right, level)
        if max_level == BTree.left_most_level(node.right, level + 1):
            return 1 + (1 << (max_level - level)) - 1 + BTree.count_of_node(node.right, level + 1, max_level)
        else:  # >
            return 1 + (1 << (max_level - level - 1)) - 1 + BTree.count_of_node(node.left, level + 1, max_level)

    @staticmethod
    def left_most_level(node, level):
        while node:
            level += 1
            node = node.left
        return level - 1


if __name__ == '__main__':
    bt1 = BTree(1)
    bt2 = BTree(2, bt1, bt1)
    bt3 = BTree(3, bt1)
    bt4 = BTree(4, bt2, bt3)

    bt4_str = bt4.serialize()
    print(bt4_str)
    # print(bt4.graph())
    bt4_str_str = BTree.deserialize(bt4.serialize()).serialize()
    print(bt4_str_str)
    assert bt4_str == bt4_str_str

    bt5 = BTree(7, BTree(5, BTree(6)), BTree(8))
    print(BTree.is_bsearch(bt5))

    bt6 = BTree(7, BTree(5, BTree(6)), BTree(8, None, BTree(9)))
    print(BTree.is_complete(bt6))

    btl = BTree(5, BTree(6), BTree(7))
    btr = BTree(8, BTree(9))
    bt7 = BTree(7, BTree(1, btl, btl), BTree(5, BTree(1, BTree(1)), BTree(7)))
    print(bt7.count(), btr.count(), btl.count())


    # que = deque()
    # que.append(1)
    # que.append(2)
    # print(que.pop())
