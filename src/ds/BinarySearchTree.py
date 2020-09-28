#!/bin/python3

"""
Python

Input:

Output:


"""


class BinarySearchTreeNode:

    def __init__(self, data):  # constructor of class
        self.data = data   # data for node
        self.left = None   # left leaf
        self.right = None  # right leaf
        self.level = None  # level none defined

    def __str__(self):
        return str(self.data)  # return as string


class BinarySearchTree:

    def __init__(self):  # constructor of class
        self.root = None

    def insert(self, data):  # insert binary search tree nodes
        if self.root is None:
            self.root = BinarySearchTreeNode(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = BinarySearchTreeNode(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = BinarySearchTreeNode(data)
                        break
                else:
                    break

    def minNode(self, root_node):
        current = root_node
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
        return current

    def deleteNode(self, root_node, data):

        # Base Case
        if root_node is None:
            return root_node

        # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if data < root_node.data:
            root_node.left = self.deleteNode(root_node.left, data)

        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif(data > root_node.data):
            root_node.right = self.deleteNode(root_node.right, data)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp

            elif root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minNode(root_node.right)

            # Copy the inorder successor's content to this node
            root_node.data = temp.data

            # Delete the inorder successor
            root_node.right = self.deleteNode(root_node.right, temp.data)

        return root_node

    def bft(self):  # Breadth-First Traversal
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.data) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        print(''.join(out))

    def _inorder(self, root_node):
        if root_node is not None:
            self._inorder(root_node.left)
            print(root_node.data)
            self._inorder(root_node.right)

    def inorder(self):
        self._inorder(self.root)

    def _preorder(self, root_node):
        if root_node is not None:
            print(root_node.data)
            self._preorder(root_node.left)
            self._preorder(root_node.right)

    def preorder(self):
        self._inorder(self.root)

    def _postorder(self, root_node):
        if root_node is not None:
            self._postorder(root_node.left)
            self._postorder(root_node.right)
            print(root_node.data)

    def postorder(self):
        self._inorder(self.root)
