'''
Below are some common binary tree questions, try to solve them!
'''

# Given a binary tree, find it's maximum depth


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printMaxDepth(self):
        print('The maximum depth of given binary tree is:',
              self._maxDepth(self) - 1)

    # Preorder DFS
    def printBinaryTree(self):
        print('Printing Binary Tree: ', end='')
        self._preorderDFS(self)
        print()

    def _preorderDFS(self, node):
        if node:
            print(node.data, end=' ')
            self._preorderDFS(node.left)
            self._preorderDFS(node.right)

    # Helper function for finding max depth of tree
    def _maxDepth(self, node):
        if not node:
            return 0
        else:
            # Max depth traverses tree recursively when node is not null
            leftDepth = self._maxDepth(node.left)
            rightDepth = self._maxDepth(node.right)

            # Compare after left and right traversal
            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1

# Setup for maximum depth problem
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node1.left = node2
# node2.right = node3
# node3.left = node4
# node3.right = node5
# node5.left = node6
# node1.printBinaryTree()
# node1.printMaxDepth()
