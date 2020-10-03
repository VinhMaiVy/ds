#!/bin/python3

"""
Treap with Implicit Keys

"""

# from random import randint
# from random import random
from random import Random


class Treap:

    def __init__(self, val: int, seed=0):
        global random
        if seed:
            random = Random(0)
        self.val = val
        self.priority = random.randint(0, 300)
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


def cnt(root: Treap) -> int:
    if root is None:
        return 0
    else:
        return root.size


def upd_cnt(root: Treap):
    if (root):
        root.size = 1 + cnt(root.left) + cnt(root.right)


def insert(root: Treap, index: int, treap: Treap) -> Treap:
    """
    Insert element
    """
    left, right = split(root, index)
    return merge(merge(left, treap), right)


def erase(root: Treap, index: int) -> Treap:
    """
    Erase element
    """
    left, right = split(root, index)
    _, right = split(right, 1)
    return merge(left, right)


def replace(root: Treap, index: int, treap: Treap) -> Treap:
    """
    Replace element
   """
    return insert(erase(root, index), index, treap)


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


def split(t: Treap, index: int) -> (Treap, Treap):

    if not t:
        return (None, None)

    if index <= 0:
        return (None, t)

    if index >= t.size:
        return (t, None)

    '''
    cur_key = add + cnt(t.left)
    if cur_key < index:
        t.right, right = split(t.right, index, add + 1 + cnt(t.left))
        left = t
        upd_cnt(t)
        return (left, right)
    else:
        left, t.left = split(t.left, index, add)
        right = t
        upd_cnt(t)
        return (left, right)
    '''

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


if __name__ == '__main__':

    n = 10
    arr = [i for i in range(n, 0, -1)]

    # First Node
    t = Treap(arr[0], 1)

    for a in arr[1:]:
        t = merge(t, Treap(a))
    print(t)
    # print(repr(t))

    l, r = split(t, 3)
    print(l)
    print(r)

    res = merge(r, l)
    print(t)
