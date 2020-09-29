#!/bin/python3

"""
Python

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


# from random import random
from ds.Treap2 import Treap


def handle(treap, c, i, j):

    # print('handling', t.val, c, i, end)
    i -= 1

    left, treap.root = treap.split(i)
    print(str(left))
    print(str(treap))

    treap.root, right = treap.split(j - i)
    print(str(treap))
    print(str(right))

    result = treap.merge(left, right)
    print(str(result))

    if c == 1:
        result = treap.merge(treap.root, result)
    elif c == 2:
        result = treap.merge(result, treap.root)

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
