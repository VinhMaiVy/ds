#!/bin/python3

"""
Treap with Implicit Keys

"""

from random import random


class Treap:

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index < self.left.size:
            return self.left[index]
        elif self.left and self.right and index > self.left.size:
            return self.right[index - self.left.size - 1]
        return self.val

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.val) + ' '
        res += str(self.right) if self.right else ''
        return res

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()

            name = 'p=' + str(node.priority) + '-s=' + str(node.size) + '-v=' + str(node.val) \
                if node else '*'

            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.left, indent + 1))
                nodes.append((node.right, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.size


def merge(left: Treap, right: Treap) -> Treap:
    # print('merging')
    if not (left and right):
        return left or right

    # print('left:', left.val, left.priority, left.size,
    #   'right:', right.val, right.priority, right.size)

    if left.priority > right.priority:
        left.size = left.size + right.size  # <<< size
        left.right = merge(left.right, right)
        # print('returning left:', left.val)
        return left

    # left is smaller
    right.size = right.size + left.size  # <<< size
    right.left = merge(left, right.left)
    # print('returning right:', right.val)
    return right


def split(t: Treap, index) -> (Treap, Treap):

    '''
    void split( pnode root, int k, pnode &left, pnode &right, int add = 0 ) {

      if( !root ) {
        left = right = NULL;
        return;
      }

      int cur_key = add + cnt( root->left );

      if( cur_key < k ) {
        split( root->right, k, root->right, right, add+1+cnt( root->left ) );
        left = root;
      }
      else {
        split( root->left, k, left, root->left, add );
        right = root;
      }
      upd_cnt( root );
    }

    '''

    if not t:
        return (None, None)

    if not index:
        return (None, t)

    if index >= t.size:
        # print('index == t.size, returning', t.val)
        return (t, None)

    # print('asked to split', t.val, t.size, 'on', index)
    if t.left and t.left.size >= index:
        # print('t.l.s:', t.left.size, '>=', index)
        res, t.left = split(t.left, index)
        t.size -= res.size
        return (res, t)

    index -= t.left.size if t.left else 0
    # print('index is now', index)
    if index == 1:
        # print('index is 1, cut off', t.right.val
        #  if t.right else 'None', 'and return', t.val)
        temp = t.right
        t.right = None
        t.size -= temp.size
        return (t, temp)

    # definitely to the right
    t.right, leftover = split(t.right, index - 1)
    # print('taking leftovers')
    # leftover exists because we already checked
    #  if they wanted everything at the top
    t.size -= leftover.size
    return (t, leftover)


def insert(root: Treap, val: int) -> Treap:
    """
    Insert element

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    node = Treap(val, random())
    left, right = split(root, val)
    return merge(merge(left, node), right)


def erase(root: Treap, val: int) -> Treap:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, val - 1)
    _, right = split(right, val)
    return merge(left, right)


def handle(t: Treap, key: int, start: int, end: int) -> Treap:

    # print('handling', t.val, key, start, end)
    start -= 1
    left, t = split(t, start)
    t, right = split(t, end - start)
    res = merge(left, right)

    if key == 1:
        res = merge(t, res)
    else:
        res = merge(res, t)

    return res


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # ------- a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # --------p = [5, 7, 6, 9, 2, 4, 1, 8, 3]

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # priorities = [5, 7, 6, 9, 2, 4, 1, 8, 3]

    # print('a', a)
    t = Treap(a[0], random())
    # t = Treap(a[0], priorities.pop(0))
    for i in a[1:]:
        # t = merge(t, Treap(i, random()))
        # t = merge(t, Treap(i, priorities.pop(0)))
        t = insert(t, i)

    print(t, len(t))

    # t = erase(t, 5)
    # print(t, len(t))

    l, r = split(t, 4)
    print(l, len(l))
    print(r, len(r))

    # l = erase(l, 2)
    print(l, len(l))
    t = merge(l, r)
    print(t, len(t))
    # print(repr(t))

    # for _ in range(m):
    # print(t)
    # t = handle(t, *map(int, input().split()))
    # print(abs(t[1] - t[n]))
    # print(t)
