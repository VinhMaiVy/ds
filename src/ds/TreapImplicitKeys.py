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
from random import randint


class Treap:

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index < self.left.size:
            return self.left[index]
        elif self.left and self.right and index > self.left.size:
            return self.right[index - self.left.size - 1]
        return self.val

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.val) + ' '
        res += str(self.right) if self.right else ''
        return res

    def __repr__(self):
        """Return a string representation of treap."""
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
    # print('merging')
    if not (left and right):
        return left or right

    # print('left:', left.val, left.priority, left.size,
    #   'right:', right.val, right.priority, right.size)

    if left.priority > right.priority:
        left.size = left.size + right.size  # <<< size
        left.right = merge(left.right, right)
        # print('returning left:', left.val)
        return left

    # left is smaller
    right.size = right.size + left.size  # <<< size
    right.left = merge(left, right.left)
    # print('returning right:', right.val)
    return right


def split(t: Treap, index) -> (Treap, Treap):

    if not t:
        return (None, None)

    if not index:
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


def insert(root: Treap, index: int, val: int) -> Treap:
    """
    Insert element

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    node = Treap(val, random())
    left, right = split(root, index)
    return merge(merge(left, node), right)


def append(root: Treap, t: Treap) -> Treap:
    """
    Insert Treap

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    return merge(root, t)


def erase(root: Treap, index: int) -> Treap:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, index)
    # print('l=', left, ' r=', right)
    _, right = split(right, 1)
    # print('l=', left, ' r=', right)
    return merge(left, right)


if __name__ == '__main__':

    n = 100
    a = [i for i in range(n)]

    t = Treap(a[0], randint(0, n * 10))
    for i in a[1:]:
        t = merge(t, Treap(i, randint(0, n * 10)))

    print(t)
    print(repr(t))
