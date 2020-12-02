from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def connect(root: 'Node') -> 'Node':
    if not root: return root
    if root.left:
        root.left.next = root.right
        connect(root.left)
    if root.right:
        if root.next:
            root.right.next = root.next.left
        connect(root.right)
    return root


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, _min, _max):
            if node is None: return True
            # left_valid, rigtht_valid = True, True
            if _max and node.val > _max.val:
                return False
            if _min and node.val < _min.val:
                return False
            return helper(node.left, _min, node) and helper(node.right, node, _max)

        return helper(root, None, None)

    def isValidBST1(self, root: TreeNode) -> bool:
        if root is None: return True
        stack = deque()
        # stack.append(root)
        prev, left_most = None, root
        while left_most or len(stack) > 0:
            # left_most = stack[-1]  # 准备放入左斜支树了
            while left_most:
                stack.append(left_most)
                left_most = left_most.left
            left_most = stack.pop()
            # its_parent = stack.pop() if len(stack) > 0 else None
            if prev and prev.val >= left_most.val:
                # or its_parent and its_parent.val <= left_most.val:
                return False
            # if not its_parent:
            #     return True

            # if its_parent.right:
            #     if its_parent.right.val <= its_parent.val:
            #         return False
            #     stack.append(its_parent.right)
            # prev_val = its_parent.val
            prev = left_most
            left_most = left_most.right
        return True

    def count_nodes_of_comp_tree(self, root):
        if not root: return 0
        r, l = root, root
        llevel, rlevel = 0, 0
        count = 0
        while l:
            llevel += 1
            l = l.left
        while r:
            rlevel += 1
            r = r.right
        if llevel == rlevel:
            return 2 ** llevel - 1
        else:
            return 1 + self.count_nodes_of_comp_tree(root.left) \
                   + self.count_nodes_of_comp_tree(root.right)

    def find_duplicate_subtrees(root: TreeNode):
        map = {}
        res = []

        def traverse(node: TreeNode):
            if not node: return "#"
            me = f"{traverse(node.left)},{traverse(node.right)},{node.val}"
            if me not in map:
                map[me] = node
            # map[me] += 1
            elif map[me]:
                res.append(node)
                map[me] = None
            return me

        traverse(root)
        return res

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        rfirst = root.right
        llast = root.left
        self.flatten(root.left)
        self.flatten(root.right)
        while llast and llast.right:
            llast = llast.right
        if llast:
            root.right = root.left
            root.left = None
            llast.right = rfirst
            llast.left = None


def test1():
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n1.left = n2
    print(Solution().isValidBST1(n1))

    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n1.right = n2
    print(Solution().isValidBST1(n1))

    n1 = TreeNode(10)
    n2 = TreeNode(5)
    n3 = TreeNode(15)
    n3.left = TreeNode(14)
    n3.right = TreeNode(20)
    n1.left = n2
    n1.right = n3
    print(Solution().isValidBST1(n1))


if __name__ == '__main__':
    test1()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n3.left = TreeNode(4)
    n3.right = TreeNode(5)
    n1.left = n3
    n1.right = n2
    print(Solution().count_nodes_of_comp_tree(n1))

