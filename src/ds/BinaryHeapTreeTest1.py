'''
Created on Sep 21, 2020

@author: vinhm

Input:
10
5 3 2 1 6 7 8 9 10 4

Output:


'''
from ds.BinaryHeapTree import BinaryHeapTree

if __name__ == '__main__':

    # t = int(input())
    t = 10

    heap = BinaryHeapTree(t)

    # arr = list(map(int, input().split()))
    arr = [5, 3, 2, 1, 6, 7, 8, 9, 10, 4]

    for a in arr:
        heap.insert(a)

    print(heap)
