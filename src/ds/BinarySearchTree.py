'''
Created on Sep 21, 2020

@author: vinhm
'''


class BinarySearchTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BinarySearchTreeNode(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = BinarySearchTreeNode(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = BinarySearchTreeNode(val)
                        break
                else:
                    break

    def delete(self, val):
        pass

    def min(self):
        if not self.root.left:
            return self.root.data
        else:
            current = self.root
            while current.left:
                current = current.left
            return current.data

    def max(self):
        if not self.root.right:
            return self.root.data
        else:
            current = self.root
            while current.right:
                current = current.right
            return current.data
