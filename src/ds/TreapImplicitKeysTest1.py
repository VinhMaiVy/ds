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
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index <= self.left.size:
            return self.left[index]

        index -= self.left.size if self.left else 0

        if index == 1:
            return self.val

        return self.right[index - 1]

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

            name = 'p=' + str(node.priority) + '-s=' + str(node.size) + '-v=' + str(node.val) \
                if node else '*'

            lines.append('  ' * indent + name)
            if node:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.size


def merge(left: Treap, right: Treap) -> Treap:
    if not (left and right):
        return left or right
    if left.priority > right.priority:
        left.size = left.size + right.size
        left.right = merge(left.right, right)
        return left
    right.size = right.size + left.size
    right.left = merge(left, right.left)
    return right


def split(t: Treap, index: int) -> (Treap, Treap):

    if not t:
        return (None, None)
    if index <= 0:
        return (None, t)
    if index >= t.size:
        return (t, None)

    if t.left and t.left.size >= index:
        res, t.left = split(t.left, index)
        t.size = t.size - res.size
        return (res, t)

    index -= t.left.size if t.left else 0
    if index == 1:
        temp = t.right
        t.right = None
        t.size = t.size - temp.size
        return (t, temp)

    t.right, leftover = split(t.right, index - 1)
    t.size = t.size - leftover.size
    return (t, leftover)


def handle(t, key, start, end):
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
    t = Treap(a[0])
    for i in a[1:]:
        t = merge(t, Treap(i))
    for _ in range(m):
        t = handle(t, *map(int, input().split()))
    print(abs(t[1] - t[n]))
    print(t)
