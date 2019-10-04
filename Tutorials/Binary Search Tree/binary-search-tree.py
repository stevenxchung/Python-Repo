'''
Given a binary search tree is a binary tree where all values to the right are bigger than the values to the left: implement a binary search tree
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return search(root.right, key)
        else:
            return search(root.left, key)

    def binarySearch(self, arr, l, r, x):
        # Code here

        # Test binary search
bst = BinarySearchTree()
