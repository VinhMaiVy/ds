#!/bin/python3

"""
Treap with Implicit Keys

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
        if (root.left is not None):
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        if index == 1:
            return root.val
        return self._getitem(root.right, index - 1)  # Must have right

    def __getitem__(self, index):
        if 0 <= index < self.cnt:
            return self._getitem(self, index + 1)
        else:
            return None

    def _setitem(self, root, index, val: int):
        if (root.left is not None):
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

    if root is None:
        return (None, None)

    cur_ind = root.left.cnt if (root.left is not None) else 0
    cur_ind += add
    if index < cur_ind:
        resleft, root.left = split(root.left, index, add)
        resright = root
        resright.cnt -= resleft.cnt if (resleft is not None) else 0  # <<<- cnt
    else:
        root.right, resright = split(root.right, index, cur_ind + 1)
        resleft = root
        resleft.cnt -= resright.cnt if (resright is not None) else 0  # <- cnt

    # upd_minimum(root)
    return resleft, resright


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


if __name__ == '__main__':

    R = Random()
    n = 10
    arr = R.sample(range(0, n), n)

    t = None
    for a in arr:
        t = merge(t, Treap(a))
    print('Max depth=', maxDepth(t))
    print(t)
    l, r = split(t, len(t) // 3 - 1)
    m, r = split(r, (len(t) * 2) // 3 - 1)
    print(l, '-', m, '-', r)
    t = merge(merge(r, m), l)
    print(t)
    print('pre--', preorder(t))
    print('in----', inorder(t))
    print('post--', postorder(t))
    # print(repr(t))
    print(" ".join([str(t[i]) for i in range(len(t))]))

    # print(t)
    # t = insert(t, 2, 8)
    # print(repr(t))
    l, r = split(t, 0)
    print(l)
    print(r)

    # print(t, t[0], t[len(t) - 1])
    # print(repr(t))
