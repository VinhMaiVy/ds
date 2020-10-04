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

from random import random


class Treap:

    def __init__(self, val: int):
        self.val = val
        self.priority = random()
        self.cnt = 1
        self.minimum = val
        self.right = None
        self.left = None

    def _getitem(self, root, index):
        if root.left and (index <= root.left.cnt):
            return self._getitem(root.left, index)
        index -= root.left.cnt if root.left else 0
        if index == 1:
            return root.val
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        if index < 0 and index > self.cnt:
            return None
        else:
            return self._getitem(self, index + 1)

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

    '''
    def __len__(self):
        return self.cnt
    '''


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
        left.cnt = left.cnt + right.cnt  # <<<----------------- cnt
        left.right = merge(left.right, right)
        res = left
    else:
        right.cnt = right.cnt + left.cnt  # <<<---------------- cnt
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
    left, right = split(root, index)
    _, right = split(right, 1)
    root = merge(left, right)
    return root


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
