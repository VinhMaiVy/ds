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

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index <= self.left.size:
            return self.left[index]
        index -= self.left.size if self.left else 0
        if index == 1:
            return self.data
        return self.right[index - 1]

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.data) + ' '
        res += str(self.right) if self.right else ''
        return res


def split(t, index):
        if not index:
            return None, t
        if not t:
            return None, None

        # print('asked to split', t.data, t.size, 'on', index)

        if index == t.size:
            # print('index == t.size, returning', t.data)
            return t, None

        if t.left and t.left.size >= index:
            # print('t.l.s:', t.left.size, '>=', index)
            res, t.left = split(t.left, index)
            t.size -= res.size
            return res, t

        index -= t.left.size if t.left else 0
        # rint('index is now', index)
        if index == 1:
            # print('index is 1, cut off', t.right.data
            # if t.right else 'None', 'and return', t.data)
            temp = t.right
            t.right = None
            t.size -= temp.size
            return t, temp

        # definitely to the right
        t.right, leftover = split(t.right, index - 1)
        # print('taking leftovers')
        t.size -= leftover.size
        # leftover exists because we already checked
        # if they wanted everyhing at the top
        return t, leftover


def merge(left, right):  # print('merging')
        if not (left and right):
            return left or right

        if left.priority > right.priority:
            left.size += right.size
            left.right = merge(left.right, right)
            # print('returning left:', left.data)
            return left

        # left is smaller
        right.size += left.size
        right.left = merge(left, right.left)
        # print('returning right:', right.data)
        return right


def handle(t, c, i, j):

    i -= 1

    left, t = split(t, i)
    # print('left: ', left)
    t, right = split(t, j - i)
    # print('right: ', right)
    result = merge(left, right)
    # print('merge: ', result)
    # print('cut: ', t)

    if c == 1:
        result = merge(t, result)
    elif c == 2:
        result = merge(result, t)

    # print('result: ', result, '\n')
    return result


if __name__ == '__main__':

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    t = Treap(a[0], random())
    for i in a[1:]:
        t = merge(t, Treap(i, random()))

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    for c, i, j in queries:
        t = handle(t, c, i, j)

    print(abs(t[1] - t[n]))
    print(t)
