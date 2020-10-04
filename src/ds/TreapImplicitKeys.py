#!/bin/python3

"""
Treap with Implicit Keys

"""

from random import random


class Treap:

    def __init__(self, val: int):
        self.val = val
        self.priority = random()
        self.cnt = 1
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

            name = 'p=' + str(node.priority * 1000)[0:2] + '-s=' + str(node.cnt) + '-v=' + str(node.val) \
                if node else '*'

            lines.append('   ' * indent + name)
            if node:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt


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


def insert(root: Treap, index: int, val: int) -> Treap:
    """
    Insert element
    """
    left, right = split(root, index)
    return merge(merge(left, Treap(val)), right)


def erase(root: Treap, index: int) -> Treap:
    """
    Erase element
    """
    left, right = split(root, index)
    _, right = split(right, 1)
    return merge(left, right)


def replace(root: Treap, index: int, val: int) -> Treap:
    """
    Replace element
   """
    root = erase(root, index)
    print(root)
    root = insert(root, index, val)
    print(root)
    return root


def merge(left: Treap, right: Treap) -> Treap:
    # print('merging')
    if not (left and right):
        return left or right

    # print('left:', left.val, left.priority, left.cnt,
    #   'right:', right.val, right.priority, right.cnt)
    if left.priority > right.priority:
        left.cnt = left.cnt + right.cnt  # <<<---------------- cnt
        left.right = merge(left.right, right)
        # print('returning left:', left.val)
        return left

    # left is smaller
    right.cnt = right.cnt + left.cnt  # <<<------------------- cnt
    right.left = merge(left, right.left)
    # print('returning right:', right.val)
    return right


def split(root: Treap, index: int) -> (Treap, Treap):

    if not root:
        return (None, None)

    if root.left and root.left.cnt >= index:
        res, root.left = split(root.left, index)
        root.cnt = root.cnt - res.cnt  # <<<------------------ cnt
        return (res, root)

    index -= root.left.cnt if root.left else 0  # <<<--------- cnt

    if index == 1:
        temp = root.right
        root.right = None
        root.cnt -= temp.cnt if temp else 0  # <<<------------ cnt
        return (root, temp)

    root.right, leftover = split(root.right, index - 1)
    root.cnt = root.cnt - leftover.cnt  # <<<----------------- cnt
    return (root, leftover)


if __name__ == '__main__':

    n = 10
    arr = [7, 8, 9, 3, 4, 5, 6, 0, 1, 2]

    # First Node
    t = Treap(arr[0])

    for a in arr[1:]:
        t = merge(t, Treap(a))
    print(t)

    l, r = split(t, 3)
    m, r = split(r, 4)
    t = merge(merge(r, m), l)

    print('prep--', preorder(t))
    print('in----', inorder(t))
    print('post--', postorder(t))
    # print(repr(t))

    print(" ".join([str(t[i]) for i in range(9)]))

    t = replace(t, 5, 2)
    print(t)

    t = insert(t, 2, 8)
    # print(repr(t))
    print(t, t[0], t[9])
