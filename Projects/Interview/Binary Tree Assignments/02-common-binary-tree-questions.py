'''
Below are some common binary tree questions, try to solve them!
'''

# Given a binary tree, find it's maximum depth


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Depth of the tree is based on head node starting at 1 to the furthest leaf node
    def printMaxDepth(self):
        print('The maximum depth of given binary tree is:',
              self._maxDepth(self) - 1)

    # Height of the tree is based on head node starting at 0 to the furthest leaf node
    def printMaxHeight(self):
        print('The maximum height of given binary tree is:',
              self._maxDepth(self))

    # Preorder DFS
    def printBinaryTree(self):
        print('Printing Binary Tree: ', end='')
        self._preorderDFS(self)
        print()

    def isSymmetric(self):
        print('Is this tree symmetric?', end=' ')
        # print(self is None or self._isMirror(self.left, self.right))
        print(self is None or self._isMirrorIterative())

    def _isMirrorIterative(self):
        node = self
        if node.left is None and node.right is None:
            return True

        queue = []

        # We append two copies of node since we want to compare left and right
        queue.append(node)
        queue.append(node)
        left = 0
        right = 0

        # Run until queue is empty
        while len(queue) > 0:
            # Compare first two nodes in queue through each test
            left = queue[0]
            queue.pop(0)
            right = queue[0]
            queue.pop(0)

            if left.data != right.data:
                return False
            if left.left and right.right:
                queue.append(left.left)
                queue.append(right.right)
            elif left.left or right.right:
                return False
            if left.right and right.left:
                queue.append(left.right)
                queue.append(right.left)
            elif left.right or right.left:
                return False

        # Only when all tests have passed can a tree be symmetric
        return True

    def _isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            return left.data == right.data and self._isMirror(left.left, right.right) and self._isMirror(left.right, right.left)
        else:
            return False

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


# Setup for symmetric tree problem
node1 = Node(1)
node3 = Node(3)
node4 = Node(4)
leftTree = Node(2)
leftTree.left = node3
leftTree.right = node4
rightTree = Node(2)
rightTree.left = node4
rightTree.right = node3
node1.left = leftTree
node1.right = rightTree
node1.printBinaryTree()
node1.printMaxDepth()
node1.printMaxHeight()
node1.isSymmetric()
