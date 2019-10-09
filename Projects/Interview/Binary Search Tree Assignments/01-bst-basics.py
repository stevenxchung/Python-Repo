'''
A BST (binary search tree) is a binary tree where:
  a. The value in each node to its left subtree is less than the current node
  b. The value in each node to its right subtree is greater than the current node

Looking up a value takes O(log(n)) if the tree is balanced and O(h) is the height of the tree

Implement the following:
1. Search in a BST
2. Insert into a BST
3. Delete Node in a BST
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        node = self
        queue = []
        queue.append(node)

        print('Printing BST in Level Order:', end=' ')
        while len(queue) > 0:

            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print()


# Test
node2 = Node(2, Node(1), Node(3))
head = Node(4, node2, Node(6))
head.printTree()
