'''
Below are some common binary tree questions, try to solve them!
'''

# Given a binary tree, find it's maximum depth


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printTree(self):
        node = self
        stack = []
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
node1.left = node2
node2.right = node3
node3.left = node4
node3.right = node5
node1.printTree()
