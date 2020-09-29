#!/usr/bin/env python3

"""
Treap

"""

# import random


class Treap:

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None
        self.level = None

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

    def bft(self):  # Breadth-First Traversal
        self.level = 0
        queue = [self]
        out = []
        current_level = self.level

        out.append("Treap:\n")
        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append('[' + str(current_node.val) +
                       ',' + str(current_node.priority) +
                       ',' + str(current_node.size) +
                       ' l={ ' + str(current_node.left) +
                       '} r={ ' + str(current_node.right) + '}] ')

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        print(''.join(out), '\n')


def merge(left, right):
    if debug:
        print('merging')
        print('left:', left, 'right:', right)

    if not (left and right):
        return left or right

    if debug:
        print('left:', left.val, left.priority, left.size,
              'right:', right.val, right.priority, right.size)

    if left.priority > right.priority:
        left.size += right.size
        left.right = merge(left.right, right)
        if debug:
            print('returning left:', left.val)
        return left

    # left is smaller
    right.size += left.size
    right.left = merge(left, right.left)
    if debug:
        print('returning right: ', right.val)
    return right


def split(t, index):

    if not index:
        return None, t

    if not t:
        return None, None

    if debug:
        print('asked to split: ', t.val, t.size, 'on', index)

    if index == t.size:
        if debug:
            print('index == ', t.size, ' returning: ', t.val)

        return t, None

    if t.left and t.left.size >= index:
        if debug:
            print('t.l.s:', t.left.size, '>=', index)
        res, t.left = split(t.left, index)
        t.size -= res.size
        return res, t

    index -= t.left.size if t.left else 0
    if debug:
        print('index is now', index)
    if index == 1:
        if debug:
            print('index is 1, cut off', t.right.val
                  if t.right else 'None', 'and return', t.val)
        temp = t.right
        t.right = None
        t.size -= temp.size
        return t, temp

    # definitely to the right
    t.right, leftover = split(t.right, index - 1)
    if debug:
        print('taking leftovers')
    t.size -= leftover.size
    # leftover exists because we already checked
    # if they wanted everything at the top
    return t, leftover


if __name__ == '__main__':
    debug = False
    # n, m = map(int, input().split())
    # n, m = 10, 4
    n = 10
    # a = list(map(int, input().split()))
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a = [i for i in range(n)]
    # priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # priorities = random.sample(range(0, n), n)
    priorities = [4, 8, 5, 1, 6, 9, 3, 0, 2, 7]
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
    left, t = split(t, 3)
    print('left: ', left)
    left.bft()
    print('t: ', t)
    t, right = split(t, 4)
    print('right: ', right)
    res = merge(left, right)
    print('merge: ', res)
    print('t: ', t)

    # print('\na[0]-a[n-1]:', abs(t[1] - t[n]))
    # print('t: ', t)
