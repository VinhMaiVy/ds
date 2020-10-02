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
        self.root.priority = random.randrange(2 ** 16)

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

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node.root) if node else 'None'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.root.right, indent + 1))
                nodes.append((node.root.left, indent + 1))
        return "\n".join(lines)


def splitTreap(t: Treap, index: int) -> (Treap, Treap):
        if not index:
            return None, t
        if not t:
            return None, None

        if index == t.root.size:
            return t, None

        if t.root.left and t.root.left.root.size >= index:
            res, t.root.left = splitTreap(t.root.left, index)
            t.root.size -= res.root.size
            return res, t

        index -= t.root.left.root.size if t.root.left else 0
        if index == 1:
            temp = t.root.right
            t.root.right = None
            t.root.size -= temp.root.size
            return t, temp
        t.root.right, leftover = splitTreap(t.root.right, index - 1)
        t.root.size -= leftover.root.size
        return t, leftover


def mergeTreap(l: Treap, r: Treap) -> Treap:
        if not (l and r):
            return l or r

        if l.root.priority > r.root.priority:
            l.root.size += r.root.size
            l.root.right = mergeTreap(l.root.right, r)
            return l

        r.root.size += l.root.size
        r.root.left = mergeTreap(l, r.root.left)

        return r


def handleTreap(t: Treap, c: int, i: int, j: int):

    i -= 1

    left, t = splitTreap(t, i)
    t, right = splitTreap(t, j - i)
    result = mergeTreap(left, right)

    if c == 1:
        result = mergeTreap(t, result)
    elif c == 2:
        result = mergeTreap(result, t)

    return result


if __name__ == '__main__':

    random = Random(0)

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    t = Treap(TreapNode(a[0]), random)
    for i in a[1:]:
        t = mergeTreap(t, Treap(TreapNode(i), random))

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    for c, i, j in queries:
        t = handleTreap(t, c, i, j)
        # print(t)

    print(abs(t[1] - t[n]))
    print(t)
