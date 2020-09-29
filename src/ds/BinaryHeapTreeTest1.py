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

    t = int(input())

    heap = BinaryHeapTree(t)

    arr = list(map(int, input().split()))

    heap.heapify(arr)

    while not heap.heapEmpty():
        print(heap.pop())
