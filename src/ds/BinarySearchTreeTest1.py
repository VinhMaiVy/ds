'''
Created on Sep 21, 2020

@author: vinhm

Input:
6
4 2 3 1 7 6

Output:


'''
from ds.BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.insert(arr[i])

    print('tree root is:', tree.root)
    print('tree min is:', tree.min())
    print('tree max is:', tree.max())
    
    tree.sort()    
