#!/usr/bin/env python3

from random import randint


class TreapNode(object):

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.left = None
        self.right = None


class Treap(object):

    @staticmethod
    def gen():
        return randint(1, 2**64)

    def __init__(self):
        self.root = None

    def split(self, tp_node, data):
        if tp_node is None:
            return (None, None)
        if data < tp_node.data:
            left, tp_node.left = self.split(tp_node.left, data)
            right = tp_node
            return (left, right)
        else:
            tp_node.right, right = self.split(tp_node.right, data)
            left = tp_node
            return (left, right)

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def find(self, tp_node, data):
        if tp_node is None:
            return False
        if tp_node.data == data:
            return True
        elif data < tp_node.data:
            return self.find(tp_node.left, data)
        else:
            return self.find(tp_node.right, data)

    def insert(self, data):
        new_node = TreapNode(data, self.gen())
        if self.root is None:
            self.root = new_node
            return
        LEFT, RIGHT = self.split(self.root, data - 1)
        self.root = self.merge(LEFT, new_node)
        self.root = self.merge(self.root, RIGHT)

    def get_height(self, tp_node):
        if tp_node is None:
            return 0
        result = 1
        result = max(result, self.get_height(tp_node.left) + 1)
        result = max(result, self.get_height(tp_node.right) + 1)
        return result

    def height(self):
        return self.get_height(self.root)
