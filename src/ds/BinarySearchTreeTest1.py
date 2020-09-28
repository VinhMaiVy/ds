'''
Created on Sep 21, 2020

@author: vinhm

Input:
10
4 2 8 3 1 10 7 6 9 5

Output:


'''

from src.ds.BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.insert(arr[i])

    tree.deleteNode(5)

    print('Breadth-First Traversal')
    tree.bft()
    print('Inorder Traversal')
    tree.inorder()
    print('Preorder Traversal')
    tree.preorder()
    print('Postorder Traversal')
    tree.postorder()
