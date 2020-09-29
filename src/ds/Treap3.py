#!/usr/bin/env python3

"""
Treap

Input:
8 4
4 8 5 3 1 2 7 6
1 2 4
2 3 5
1 4 7
2 1 4

Output:
1
2 3 6 5 7 8 4 1


"""


from random import randint


class TreapNode(object):

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.left = None
        self.right = None

    def __str__(self):
        res = self.__str__(self.left) if self.left else ''
        res += str(self.data) + ' '
        res += self.__str__(self.right) if self.right else ''
        return res

    def __getitem__(self, key):
        if self is None:
            return False
        if self.data == key:
            return True
        elif key < self.data:
            return self.__getitem__(self.left, key)
        else:
            return self.__getitem__(self.right, key)


class Treap(object):

    def __init__(self, tnode=None):
        if tnode:
            self.root = tnode
        else:
            self.root = None

    @staticmethod
    def gen():
        return randint(1, 2**64)

    def insert(self, data):
        new_node = TreapNode(data, self.gen())
        if self.root is None:
            self.root = new_node
            return
        LEFT, RIGHT = self._split(self.root, data - 1)
        self.root = self.merge(LEFT, new_node)
        self.root = self.merge(self.root, RIGHT)

    def _height(self, tp_node):
        if tp_node is None:
            return 0
        result = 1
        result = max(result, self.get_height(tp_node.left) + 1)
        result = max(result, self.get_height(tp_node.right) + 1)
        return result

    def height(self):
        return self._height(self.root)


def split(tnode, data):
        if tnode is None:
            return (None, None)
        if data < tnode.data:
            left, tnode.left = split(tnode.left, data)
            right = tnode
            return (left, right)
        else:
            tnode.right, right = split(tnode.right, data)
            left = tnode
            return (left, right)


def merge(left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.priority > right.priority:
            left.right = merge(left.right, right)
            return left
        else:
            right.left = merge(left, right.left)
            return right


def handle(treap, c, i, j):

    # print('handling', t.val, c, i, end)
    i -= 1

    left, treap = split(treap, i)
    print(left)

    treap, right = split(treap, j - i)
    print(right)

    result = merge(treap, left, right)
    print(result)
    print(treap)

    if c == 1:
        result = merge(treap, result)
    elif c == 2:
        result = merge(result, treap)

    return result


if __name__ == '__main__':

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    treap = Treap()

    for i in a:
        treap.insert(i)
    print(treap)

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    for c, i, j in queries:
        treap = handle(treap, c, i, j)

    print(abs(treap[1] - treap[n]))
    print(str(treap))
