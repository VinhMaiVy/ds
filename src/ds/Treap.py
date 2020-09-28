#!/bin/python3

"""
Python

Input:

Output:


"""


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

    def merge(self, left, right):  # print('merging')
        if not (left and right):
            return left or right

        if left.priority > right.priority:
            left.size += right.size
            left.right = self.merge(left.right, right)
            # print('returning left:', left.data)
            return left

        # left is smaller
        right.size += left.size
        right.left = self.merge(left, right.left)
        # print('returning right:', right.data)
        return right

    def split(self, index):
        if not index:
            return None, self
        if not self:
            return None, None

        # print('asked to split', t.data, t.size, 'on', index)

        if index == self.size:
            # print('index == t.size, returning', t.data)
            return self, None

        if self.left and self.left.size >= index:
            # print('t.l.s:', t.left.size, '>=', index)
            res, self.left = self.left.split(index)
            self.size -= res.size
            return res, self

        index -= self.left.size if self.left else 0
        # rint('index is now', index)
        if index == 1:
            # print('index is 1, cut off', t.right.data
            # if t.right else 'None', 'and return', t.data)
            temp = self.right
            self.right = None
            self.size -= temp.size
            return self, temp

        # definitely to the right
        self.right, leftover = self.right.split(index - 1)
        # print('taking leftovers')
        self.size -= leftover.size
        # leftover exists because we already checked
        # if they wanted everyhing at the top
        return self, leftover
