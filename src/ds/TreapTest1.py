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


from random import random
from src.ds.Treap1 import Treap


def handle(treap, c, i, j):

    left, treap.root = treap.split(i)
    # print('left: ', left)
    treap.root, right = treap.split(j - i)
    # print('right: ', right)
    result = treap.merge(left, right)
    # print('merge: ', result)
    # print('cut: ', treap.root)

    if c == 1:
        result = treap.merge(treap.root, result)
    elif c == 2:
        result = treap.merge(result, treap.root)

    # print('result: ', result, '\n')
    return result


if __name__ == '__main__':

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    treap = Treap(a[0], random())
    for i in a[1:]:
        treap = treap.merge(treap, Treap(i, random()))

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    for c, i, j in queries:
        treap = handle(treap, c, i-1, j)

    print(abs(treap[1] - treap[n]))
    print(treap)
