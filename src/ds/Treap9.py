#!/bin/python3

"""
Treap 9

"""


from random import Random


class TreapNode:
    """
    Treap's node
    Treap is a binary tree by data and heap by priority
    """

    def __init__(self, data: int=None, random: Random=None):
        self.data = data
        self.priority = random.randrange(2**12)
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node) if node else 'None'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.left, indent + 1))
                nodes.append((node.right, indent + 1))
        return "\n".join(lines)

    def __str__(self):
        """ Just recursive print of a tree """
        lines = []
        nodes = [self]
        while nodes:
            node = nodes.pop()
            if node:
                lines.append(str(node.data) + ' ')
            if node:
                nodes.append(node.left)
                nodes.append(node.right)
        return "".join(lines)


def splitTreap(root: TreapNode, data: int) -> (TreapNode, TreapNode):
    """
    We splitTreap current tree into 2 trees with data:

    Left tree contains all values less than splitTreap data.
    Right tree contains all values greater or equal, than splitTreap data
    """
    if root is None:  # None tree is splitTreap into 2 Nones
        return (None, None)
    elif root.data is None:
        return (None, None)
    else:
        if data > root.data:
            """
            Right tree's root will be current node.
            Now we splitTreap(with the same data) current node's left son
            Left tree: left part of that splitTreap
            Right tree's left son: right part of that splitTreap
            """
            left, root.left = splitTreap(root.left, data)
            return (left, root)
        else:
            """
            Just symmetric to previous case
            """
            root.right, right = splitTreap(root.right, data)
            return (root, right)


def mergeTreap(l: TreapNode, r: TreapNode) -> TreapNode:
    """
    We mergeTreap 2 trees into one.
    Note: all left tree's values must be less than all right tree's
    """
    if (not l) or (not r):  # If one node is None, return the other
        return l or r
    elif l.priority > r.priority:
        """
        Left will be root because it has more priority
        Now we need to mergeTreap left's right son and right tree
        """
        l.right = mergeTreap(l.right, r)
        return l
    else:
        """
        Symmetric as well
        """
        r.left = mergeTreap(l, r.left)
        return r


def insertTreap(root: TreapNode, data: int, random: Random) -> TreapNode:
    """
    Insert element

    Split current tree with a data into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    node = TreapNode(data, random)
    left, right = splitTreap(root, data)
    return mergeTreap(mergeTreap(left, node), right)


def eraseTreap(root: TreapNode, data: int) -> TreapNode:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = splitTreap(root, data - 1)
    _, right = splitTreap(right, data)
    return mergeTreap(left, right)


def inorderTreap(root: TreapNode):
    """
    Just recursive print of a tree
    """
    if not root:  # None
        return
    else:
        inorderTreap(root.left)
        print(root.data, end=" ")
        inorderTreap(root.right)


if __name__ == "__main__":

    random = Random(0)

    root = None
    root = insertTreap(root, 0, random)
    root = insertTreap(root, 8, random)
    root = insertTreap(root, 7, random)
    root = insertTreap(root, 6, random)
    root = insertTreap(root, 5, random)
    root = insertTreap(root, 4, random)
    root = insertTreap(root, 3, random)
    root = insertTreap(root, 2, random)
    root = insertTreap(root, 1, random)
    root = insertTreap(root, 9, random)
    print(repr(root))
    print(str(root))
