class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Using preorder DFS
    def printTree(self):
        node = self
        stack = []
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.right
            else:
                break


node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7)
head = Node(1, node2, node3)
head.printTree()
