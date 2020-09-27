'''
Created on Sep 21, 2020

@author: vinhm
'''


class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree():

    def __init__(self, BinarySearchTreeNode = None):
        if BinarySearchTreeNode == None:
            self.root = None
        else:
            self.root = BinarySearchTreeNode
            # print(self.root.data)

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
            return BinarySearchTree(self.root.left).min()            
            #current = self.root
            #while current.left:
            #    current = current.left
            #return current.data

    def max(self):
        if not self.root.right:
            return self.root.data
        else:
            return BinarySearchTree(self.root.right).max()
            #current = self.root
            #while current.right:
            #    current = current.right
            #return current.data

    def sort(self):
        if self.root:        
            BinarySearchTree(self.root.left).sort()
            print(self.root, end=" ")        
            BinarySearchTree(self.root.right).sort()
            