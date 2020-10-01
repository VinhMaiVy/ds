#!/bin/python3

"""
Interactive Treap

Input:

Output:


"""

from random import random
from typing import Tuple


class Node:
    """
    Treap's node
    Treap is a binary tree by value and heap by priority
    """

    def __init__(self, value: int=None):
        self.value = value
        self.prior = random()
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node.value) if node else '*'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.left, indent + 1))
                nodes.append((node.right, indent + 1))
        return "\n".join(lines)

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.value) + ' '
        res += str(self.right) if self.right else ''
        return res


def split(root: Node, value: int) -> Tuple[Node, Node]:
    """
    We split current tree into 2 trees with value:

    Left tree contains all values less than split value.
    Right tree contains all values greater or equal, than split value
    """
    if root is None:  # None tree is split into 2 Nones
        return (None, None)
    elif root.value is None:
        return (None, None)
    else:
        if value < root.value:
            """
            Right tree's root will be current node.
            Now we split(with the same value) current node's left son
            Left tree: left part of that split
            Right tree's left son: right part of that split
            """
            left, root.left = split(root.left, value)
            return (left, root)
        else:
            """
            Just symmetric to previous case
            """
            root.right, right = split(root.right, value)
            return (root, right)


def merge(left: Node, right: Node) -> Node:
    """
    We merge 2 trees into one.
    Note: all left tree's values must be less than all right tree's
    """
    if (not left) or (not right):  # If one node is None, return the other
        return left or right
    elif left.prior > right.prior:
        """
        Left will be root because it has more priority
        Now we need to merge left's right son and right tree
        """
        left.right = merge(left.right, right)
        return left
    else:
        """
        Symmetric as well
        """
        right.left = merge(left, right.left)
        return right


def insert(root: Node, value: int) -> Node:
    """
    Insert element

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    node = Node(value)
    left, right = split(root, value)
    return merge(merge(left, node), right)


def erase(root: Node, value: int) -> Node:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, value - 1)
    _, right = split(right, value)
    return merge(left, right)


def inorder(root: Node):
    """
    Just recursive print of a tree
    """
    if not root:  # None
        return
    else:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


if __name__ == "__main__":

    a = [0, 8, 7, 6, 5, 4, 3, 2, 1, 9]
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a = [0, 8, 7, 6, 2]

    root = None
    for i in range(100, 0, -1):
        # root = merge(root, Node(i))
        root = insert(root, i)

    print(repr(root))
    print(root)
