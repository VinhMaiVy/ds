#!/usr/bin/env python3

"""
Treap

"""

import random


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

    def item(self, tnode, index):
        if tnode.left and index <= tnode.left.size:
            return self.item(tnode.left, index)
        index -= tnode.left.size if tnode.left else 0
        if index == 1:
            return tnode.data
        return self.item(tnode.right, index - 1)

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
        # print('index is now', index)
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
        # if they wanted everything at the top
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


if __name__ == '__main__':
    debug = False
    # n, m = map(int, input().split())
    # n, m = 10, 4
    n = 10
    # a = list(map(int, input().split()))
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [4, 8, 5, 1, 6, 9, 3, 0, 2, 7]
    # a = [i for i in range(n)]
    # priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    priorities = random.sample(range(0, n), n)
    # priorities = [4, 8, 5, 1, 6, 9, 3, 0, 2, 7]
    print('a: ', a)
    print('p: ', priorities)

    # t = Treap(a[0], random())
    t = Treap(a[0], priorities.pop(0))
    for i in a[1:]:
        # t = merge(t, Treap(i, random()))
        t = merge(t, Treap(i, priorities.pop(0)))
        # t.bft()
    print('t: ', t)
    # queries = []
    # for _ in range(m):
    #    queries.append(list(map(int, input().split())))
    # queries = [[1, 1, 4], [2, 2, 5], [1, 3, 6], [2, 0, 4]]
    print('split(t, 3)')
    left, t = split(t, 3)
    print('left: ', left)
    print('t: ', t)

    print('split(t, 4)')
    t, right = split(t, 4)
    print('right: ', right)

    res = merge(left, right)
    print('merge: ', res)
    print(t.item(t, 1))

    # print('\na[0]-a[n-1]:', abs(t[1] - t[n]))
    # print('t: ', t)
