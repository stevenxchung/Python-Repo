class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printTreeBFS(self):
        head = self
        level = [head]
        # visited = {}
        # visited[node] = True
        print('BFS: ', end='')
        while head and level:
            nextLevel = []
            for node in level:
                print(node.data, end=' ')
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        print()

    # Using preorder DFS
    def printTreePreorder(self):
        node = self
        stack = []
        valueStack = []
        print('DFS Iterative Preorder: ', end='')
        while True:
            if node:
                stack.append(node)
                valueStack.append(node.data)
                print(node.data, end=' ')
                node = node.left
            elif stack:
                node = stack.pop()
                valueStack.pop()
                node = node.right
            else:
                break
        print()

    # Using inorder DFS
    def printTreeInorder(self):
        node = self
        stack = []
        print('DFS Iterative Inorder: ', end='')
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.right
            else:
                break
        print()


node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7)
head = Node(1, node2, node3)
head.printTreeInorder()  # 4, 2, 5, 1, 3, 6, 7
head.printTreePreorder()  # 1, 2, 4, 5, 3, 6, 7
head.printTreeBFS()  # 1, 2, 3, 4, 5, 6, 7
