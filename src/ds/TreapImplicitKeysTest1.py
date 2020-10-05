#!/bin/python3

"""
Python

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

from random import random


class Treap:

    def __init__(self, val: int):
        self.val = val
        self.priority = random()
        self.cnt = 1
        self.minimum = val
        self.right = None
        self.left = None

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        # Found!
        if index == 1:
            return root.val
        # definitely to the right
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        if 0 <= index < self.cnt:
            return self._getitem(self, index + 1)
        else:
            return None

    def _setitem1(self, root, index: int, val: int):
        if (root.left is not None):
            if index <= root.left.cnt:
                self._setitem1(root.left, index, val)
            index -= root.left.cnt
        # Found!
        if index == 1:
            root.val = val
        elif index > 1:  # definitely to the right
            self._setitem1(root.right, index - 1, val)

    def _setitem2(self, root, index: int, val: int, add=0):

        cur_ind = root.left.cnt if (root.left is not None) else 0
        cur_ind += add
        if (index < cur_ind):
            self._setitem2(root.left, index, val, add)
        elif (index > cur_ind):
            self._setitem2(root.right, index, val, cur_ind + 1)
        elif (index == cur_ind):
            root.val = val

    def __setitem__(self, index, val: int):
        if 0 <= index < self.cnt:
            self._setitem1(self, index + 1, val)

    def __str__(self):
        res = str(self.left) if (self.left is not None) else ''
        res += str(self.val) + ' '
        res += str(self.right) if (self.right is not None) else ''
        return res

    def __repr__(self):
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()

            name = 'p=' + str(node.priority * 100)[0:2] + '-c=' + str(node.cnt) + '-v=' + str(node.val)\
                if (node is not None) else '*'

            lines.append('   ' * indent + name)
            if node is not None:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt


def maxDepth(root: Treap) -> int:
    if (root is None):
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1


def preorder(root: Treap) -> str:
    res = str(root.val) + ' '
    res += preorder(root.left) if (root.left is not None) else ''
    res += preorder(root.right) if (root.right is not None) else ''
    return res


def inorder(root: Treap) -> str:
    res = inorder(root.left) if (root.left is not None) else ''
    res += str(root.val) + ' '
    res += inorder(root.right) if (root.right is not None) else ''
    return res


def postorder(root: Treap) -> str:
    res = postorder(root.left) if (root.left is not None) else ''
    res += postorder(root.right) if (root.right is not None) else ''
    res += str(root.val) + ' '
    return res


def minimum(root: Treap) -> int:
    if (root is not None):
        return float('inf')
    else:
        return root.minimum


def upd_minimum(root: Treap):
    if (root is not None):
        root.minimum = min(root.val, min(minimum(root.left),
                                         minimum(root.right)))


def merge(left: Treap, right: Treap) -> Treap:

    if (left is None) or (right is None):
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

    if (root is None):
        return (None, None)

    cur_ind = root.left.cnt if (root.left is not None) else 0
    cur_ind += add

    if index < cur_ind:
        resleft, root.left = split(root.left, index, add)
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        return resleft, root
    elif index > cur_ind:
        root.right, resright = split(root.right, index, cur_ind + 1)
        root.cnt -= resright.cnt if (resright is not None) else 0
        return root, resright
    else:
        resleft = root.left
        root.left = None
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        return resleft, root


def insertAt(root: Treap, index: int, val: int) -> Treap:
    if root is None:
        return Treap(val)
    else:
        left, right = split(root, index)
        left = merge(left, Treap(val))
        root = merge(left, right)
        return root


def eraseAt(root: Treap, index: int) -> Treap:
    left, right = split(root, index)
    _t, right = split(right, 1)
    del _t
    return merge(left, right)


def append(root: Treap, val: int) -> Treap:
    return merge(root, Treap(val))


def appendleft(root: Treap, val: int) -> Treap:
    return merge(Treap(val), root)


def tpop(root: Treap) -> (Treap, int):
    _last = len(root) - 1
    val = root[_last]
    left, right = split(root, _last)
    _t, right = split(right, 1)
    del _t
    return (merge(left, right), val)


def tpopleft(root: Treap) -> (Treap, int):
    val = root[0]
    left, right = split(root, 0)
    _t, right = split(right, 1)
    del _t
    return (merge(left, right), val)


def handle(t, key, start, end):

    # print('handling', t.val, key, start, end)
    start -= 1
    left, t = split(t, start)
    t, right = split(t, end - start)
    res = merge(left, right)

    if key == 1:
        res = merge(t, res)
    else:
        res = merge(res, t)

    return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    t = None
    for i in a:
        t = merge(t, Treap(i))

    for _ in range(m):
        t = handle(t, *map(int, input().split()))

    print(abs(t[0] - t[n - 1]))
    print(t)
