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


class Treap:

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.key) + ' '
        res += str(self.right) if self.right else ''
        return res


def split(root: Treap, key: int) -> (Treap, Treap):

    if root is None:
        return (None, None)

    if (key < root.key):
        left, root.left = split(root.left, key)
        return (left, root)
    else:
        t.right, right = split(root.right, key)
        return (root, right)


def merge(l: Treap, r: Treap) -> Treap:
    if (not l) or (not r):  # If one node is None, return the other
        return l or r
    elif l.priority > r.priority:
        """
        Left will be root because it has more priority
        Now we need to mergeTreap left's right son and right tree
        """
        l.right = merge(l.right, r)
        return l
    else:
        """
        Symmetric as well
        """
        r.left = merge(l, r.left)
        return r


def insert1(root: Treap, x: Treap) -> Treap:
    """
    Insert element

    Split current tree with a key into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    left, right = split(root, x.key)
    return merge(merge(left, x), right)


def erase1(root: Treap, key: int) -> Treap:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, key - 1)
    _, right = split(right, key)
    return merge(left, right)


def insert(root: Treap, x: Treap) -> Treap:

    if not root:
        return x
    elif x.priority > root.priority:
        x.left, x.right = split(root, x.key)
        return x
    elif x.key < root.key:
        root.left = insert(root.left, x)
        return root
    else:
        root.right = insert(root.right, x)
        return root


def erase(root: Treap, key: int) -> Treap:
    if not root:
        return
    if root.key == key:
        return merge(root.left, root.right)
    elif key < root.key:
        erase(root.left, key)
    else:
        erase(root.right, key)


if __name__ == '__main__':

    # a = [0, 8, 7, 6, 5, 4, 3, 2, 1, 9]
    a = [0, 8, 7, 6, 2]

    random = Random(0)
    t = Treap(a[0], random.randrange(2 ** 16))
    for i in a[1:]:
        # t = merge(t, Treap(i, random.randrange(2 ** 16)))
        t = insert1(t, Treap(i, random.randrange(2 ** 16)))
    print(t)
