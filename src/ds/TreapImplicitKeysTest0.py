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

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
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


def merge(left, right):
    # print('merging')
    if not (left and right):
        return left or right

    # print('left:', left.val, left.priority, left.size,
    # 'right:', right.val, right.priority, right.size)

    if left.priority > right.priority:
        left.size += right.size
        left.right = merge(left.right, right)
        # print('returning left:', left.val)
        return left

    # left is smaller
    right.size += left.size
    right.left = merge(left, right.left)
    # print('returning right:', right.val)
    return right


def split(t, index):
    if not index:
        return None, t
    if not t:
        return None, None

    # print('asked to split', t.val, t.size, 'on', index)

    if index == t.size:
        # print('index == t.size, returning', t.val)
        return t, None

    if t.left and t.left.size >= index:
        # print('t.l.s:', t.left.size, '>=', index)
        res, t.left = split(t.left, index)
        t.size -= res.size
        return res, t

    index -= t.left.size if t.left else 0
    # print('index is now', index)
    if index == 1:

        temp = t.right
        t.right = None
        t.size -= temp.size if temp else 0
        return t, temp

    # definitely to the right
    t.right, leftover = split(t.right, index - 1)
    # print('taking leftovers')
    # leftover exists because we already checked if they wanted
    # everything at the top
    t.size -= leftover.size
    return t, leftover


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
    # priorities = [5, 7, 6, 9, 10, 1, 0, 3]
    # print('a', a)
    t = Treap(a[0], random())
    # t = Treap(a[0], priorities.pop())
    for i in a[1:]:
        t = merge(t, Treap(i, random()))
        # t = merge(t, Treap(i, priorities.pop()))

    for _ in range(m):
        # print(t)
        t = handle(t, *map(int, input().split()))
    print(abs(t[1] - t[n]))
    print(t)
