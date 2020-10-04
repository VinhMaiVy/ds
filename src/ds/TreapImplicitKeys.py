#!/bin/python3

"""
Treap with Implicit Keys

Input:
8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4

Output:
1
2 3 6 5 7 8 4 1


"""
# import math
from random import Random
# from random import random


class Treap:

    def __init__(self, val: int):
        global R
        self.val = val
        self.priority = R.random()
        self.cnt = 1
        self.minimum = val
        self.right = None
        self.left = None

    def _getitem(self, root, index) -> int:
        if root.left:
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        if index == 1:
            return root.val
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        if index < 0 and index > self.cnt:
            return None
        else:
            return self._getitem(self, index + 1)

    def _setitem(self, root, index, val: int):
        if root.left:
            if index <= root.left.cnt:
                self._setitem(root.left, index, val)
            index -= root.left.cnt
        if index == 1:
            root.val = val
        elif index > 1:
            self._setitem(root.right, index - 1, val)

    def __setitem__(self, index, val: int):
        if 0 <= index < self.cnt:
            self._setitem(self, index + 1, val)

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.val) + ' '
        res += str(self.right) if self.right else ''
        return res

    def __repr__(self):
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()

            name = 'p=' + str(node.priority * 1000)[0:2] + '-c=' + str(node.cnt) + '-v=' + str(node.val)\
                if node else '*'

            lines.append('   ' * indent + name)
            if node:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt


def maxDepth(root: Treap) -> int:
    # Null node has 0 depth.
    if root is None:
        return 0

    # Get the depth of the left and right subtree
    # using recursion.
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    # Choose the larger one and add the root to it.
    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1


def preorder(root: Treap) -> str:
    res = str(root.val) + ' '
    res += preorder(root.left) if root.left else ''
    res += preorder(root.right) if root.right else ''
    return res


def inorder(root: Treap) -> str:
    res = inorder(root.left) if root.left else ''
    res += str(root.val) + ' '
    res += inorder(root.right) if root.right else ''
    return res


def postorder(root: Treap) -> str:
    res = postorder(root.left) if root.left else ''
    res += postorder(root.right) if root.right else ''
    res += str(root.val) + ' '
    return res


def minimum(root: Treap) -> int:
    if not root:
        return float('inf')
    else:
        return root.minimum


def upd_minimum(root: Treap):
    if root:
        root.minimum = min(root.val, min(minimum(root.left),
                                         minimum(root.right)))


def merge(left: Treap, right: Treap) -> Treap:

    if not (left and right):
        return left or right

    if left.priority > right.priority:
        left.cnt += right.cnt  # <<<-------------------------- cnt
        left.right = merge(left.right, right)
        res = left
    else:
        right.cnt += left.cnt  # <<<-------------------------- cnt
        right.left = merge(left, right.left)
        res = right

    # upd_minimum(res)
    return res


def split(root: Treap, index: int, add=0) -> (Treap, Treap):

    if not root:
        return (None, None)

    cur_key = root.left.cnt if root.left else 0
    cur_key += add
    if cur_key < index:
        root.right, right = split(root.right, index, cur_key + 1)
        root.cnt -= right.cnt if right else 0  # <<<----------- cnt
        left = root
    else:
        left, root.left = split(root.left, index, add)
        root.cnt -= left.cnt if left else 0  # <<<------------- cnt
        right = root

    # upd_minimum(root)
    return left, right


def insert(root: Treap, index: int, val: int) -> Treap:
    if root is None:
        return Treap(val)
    else:
        left, right = split(root, index)
        left = merge(left, Treap(val))
        root = merge(left, right)
        return root


def erase(root: Treap, index: int) -> Treap:
    """
    Erase element
    """
    left, right = split(root, index)
    _t, right = split(right, 1)
    del _t
    return merge(left, right)


def append(root: Treap, val: int) -> Treap:
    return merge(root, Treap(val))


if __name__ == '__main__':

    R = Random(2)
    n = 10
    arr = R.sample(range(0, n), n)

    t = None
    for a in arr:
        t = merge(t, Treap(a))
    print(t)
    print('Max depth=', maxDepth(t))

    # l, r = split(t, len(t) // 3)
    # m, r = split(r, len(t) * 2 // 3)
    # t = merge(merge(r, m), l)
    # print(t)

    print('prep--', preorder(t))
    print('in----', inorder(t))
    print('post--', postorder(t))
    # print(repr(t))
    print(" ".join([str(t[i]) for i in range(len(t))]))

    # print(t)
    # t = insert(t, 2, 8)
    # print(repr(t))
    t[9] = 99
    print(t)

    # print(t, t[0], t[len(t) - 1])
    # print(repr(t))
