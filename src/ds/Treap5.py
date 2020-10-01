#!/usr/bin/env python3

"""
Treap 5

"""

from random import Random


class TreapNode:
    """
    Treap's node
    Treap is a binary tree by value and heap by priority
    """

    def __init__(self, data: int):
        self.data = data
        self.priority = None
        self.size = 1
        self.right = None
        self.left = None

    def __repr__(self):
        return str((self.data, self.priority, self.size))

    def __str__(self):
        return str((self.data, self.priority, self.size))


class Treap:
    def __init__(self, root: TreapNode, random: Random):
        self.root = root
        self.root.priority = random.randrange(2**12)

    def __getitem__(self, index):
        if self.root.left and index <= self.root.left.root.size:
            return self.root.left[index]
        index -= self.root.left.root.size if self.root.left else 0
        if index == 1:
            return self.root.data
        return self.root.right[index - 1]

    def __str__(self):
        res = str(self.root.left) if self.root.left else ''
        res += str(self.root.data) + ' '
        res += str(self.root.right) if self.root.right else ''
        return res

    """
    def __str__(self):
        # Just recursive print of a tree
        lines = []
        nodes = [self]
        while nodes:
            node = nodes.pop()
            if node:
                lines.append(str(node.root.data) + ' ')
            if node:
                nodes.append(node.root.left)
                nodes.append(node.root.right)
        return "".join(lines)
    """

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node.root) if node else 'None'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.root.left, indent + 1))
                nodes.append((node.root.right, indent + 1))
        return "\n".join(lines)


def splitTreap(t: Treap, index: int) -> (Treap, Treap):
        if not index:
            return None, t
        if not t:
            return None, None

        # print('asked to splitTreap', t.data, t.size, 'on', index)

        if index == t.root.size:
            # print('index == t.size, returning', t.data)
            return t, None

        if t.root.left and t.root.left.root.size >= index:
            # print('t.l.s:', t.left.size, '>=', index)
            res, t.root.left = splitTreap(t.root.left, index)
            t.root.size -= res.root.size
            return res, t

        index -= t.root.left.root.size if t.root.left else 0
        # print('index is now', index)
        if index == 1:
            # print('index is 1, cut off', t.right.data
            # if t.right else 'None', 'and return', t.data)
            temp = t.root.right
            t.root.right = None
            t.root.size -= temp.root.size
            return t, temp

        # definitely to the right
        t.root.right, leftover = splitTreap(t.root.right, index - 1)
        # print('taking leftovers')
        t.root.size -= leftover.root.size
        # leftover exists because we already checked
        # if they wanted everything at the top
        return t, leftover


def mergeTreap(l: Treap, r: Treap) -> Treap:  # print('merging')
        if not (l and r):
            return l or r

        if l.root.priority > r.root.priority:
            l.root.size += r.root.size
            l.root.right = mergeTreap(l.root.right, r)
            # print('returning left:', left.data)
            return l

        # left is smaller
        r.root.size += l.root.size
        r.root.left = mergeTreap(l, r.root.left)
        # print('returning right:', right.data)
        return r


if __name__ == '__main__':

    random = Random(0)
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [0, 8, 7, 6, 5, 4, 3, 2, 1, 9]

    t = Treap(TreapNode(a[0]), random)
    for i in a[1:]:
        t = mergeTreap(t, Treap(TreapNode(i), random))

    print(repr(t))
    print(t)

    # queries = []
    # for _ in range(m):
    #    queries.append(list(map(int, input().splitTreap())))
    # queries = [[1, 1, 4], [2, 2, 5], [1, 3, 6], [2, 0, 4]]
    """
    print('splitTreap(t, 3)')
    left, t = splitTreap(t, 3)
    print('left: ', left)
    print('t: ', t)

    print('splitTreap(t, 4)')
    t, right = splitTreap(t, 4)
    print('right: ', right)

    res = mergeTreap(left, right)
    print('mergeTreap: ', res)

    t = mergeTreap(t, res)
    print('t: ', t)
    """
    # print('\na[0]-a[n-1]:', abs(t[1] - t[n]))
    # print('t: ', t)
