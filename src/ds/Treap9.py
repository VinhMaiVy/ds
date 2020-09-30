#!/bin/python3

"""
Python

Input:

Output:


"""


from random import random
from typing import Tuple


class TreapNode:
    """
    Treap's node
    Treap is a binary tree by value and heap by priority
    """

    def __init__(self, value: int = None):
        self.value = value
        self.priority = random()
        self.left = None
        self.right = None

    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return f"'{self.value}: {self.priority:.5}'"
        else:
            return pformat(
                {f"{self.value}: {self.priority:.5}": (self.left, self.right)},
                indent=1
            )

    def __str__(self):
        value = str(self.value) + " "
        left = str(self.left or "")
        right = str(self.right or "")
        return value + left + right


def split(root: TreapNode, value: int) -> Tuple[TreapNode, TreapNode]:
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


def merge(left: TreapNode, right: TreapNode) -> TreapNode:
    """
    We merge 2 trees into one.
    Note: all left tree's values must be less than all right tree's
    """
    if (not left) or (not right):  # If one node is None, return the other
        return left or right
    elif left.priority < right.priority:
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


def insert(root: TreapNode, value: int) -> TreapNode:
    """
    Insert element

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    node = TreapNode(value)
    left, right = split(root, value)
    return merge(merge(left, node), right)


def erase(root: TreapNode, value: int) -> TreapNode:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, value - 1)
    _, right = split(right, value)
    return merge(left, right)


def inorder(root: TreapNode):
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
    root = None
    root = insert(root, 6)
    root = insert(root, 4)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 9)
    root = insert(root, 7)
    root = insert(root, 3)
    root = insert(root, 3)
    root = insert(root, 3)
    print(str(root))
