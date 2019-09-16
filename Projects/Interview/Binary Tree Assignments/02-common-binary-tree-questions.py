'''
Below are some common binary tree questions, try to solve them!
'''

# Given a binary tree, find it's maximum depth


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def maxDepth(self, node):
        if not node:
            return 0
        else:
            leftDepth = self.maxDepth(node.left)
            rightDepth = self.maxDepth(node.right)

            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1

    def printMaxDepth(self):
        print('The maximum depth of given binary tree is:', self.maxDepth(self) - 1)

    # Same as iterative preorder DFS
    def printBinaryTree(self):
        node = self
        stack = []
        print('Printing Binary Tree: ', end='')
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop(0)
                print(node.data, end=' ')
                node = node.right
            else:
                break
        print()


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.left = node2
node2.right = node3
node3.left = node4
node3.right = node5
node5.left = node6
node1.printBinaryTree()
node1.printMaxDepth()
