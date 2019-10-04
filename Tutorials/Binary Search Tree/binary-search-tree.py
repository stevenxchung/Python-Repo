'''
Implement a binary search tree
'''

class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class BinaryTree:
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
