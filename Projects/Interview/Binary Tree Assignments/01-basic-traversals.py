'''
Given:
Preorder traversal: node, left, right
Inorder traversal: left, node, right
Postorder traversal: left, right, node

Write DFS for each traversal
Follow up: can you do it iteratively?
'''


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def dfs(self, traversalType):
        print('DFS Recursive ', end='')
        if traversalType == 'preorder':
            print('Preorder: ', end='')
            self._dfsHelperPreorder(self)
        elif traversalType == 'inorder':
            print('Inorder: ', end='')
            self._dfsHelperInorder(self)
        else:
            print('Postorder: ', end='')
            self._dfsHelperPostorder(self)
        print()

    def iterativePreorder(self):
        stack = []
        stack.append(self)
        print('DFS Iterative Preorder: ', end='')
        # Go through entire object and print tree for nodes that exist by first checking left then right
        while len(stack) > 0:
            node = stack.pop()
            print(node.data, end=' ')
            if node.left != None:
                stack.append(node.left)
            elif node.right != None:
                stack.append(node.right)
        print()

    def iterativeInorder(self):
        node = self
        stack = []
        # For debugging stack
        valueStack = []
        print('DFS Iterative Inorder: ', end='')
        # A little tricky but will always look for left nodes first before the right and will pop them off the stack before the right nodes
        while True:
            if node != None:
                stack.append(node)
                valueStack.append(node.data)
                node = node.left
            elif stack:
                node = stack.pop()
                valueStack.pop()
                print(node.data, end=' ')
                node = node.right
            else:
                break
        print()

    def iterativePostorder(self):
        node = self
        stack = []
        # For debugging stack
        valueStack = []
        print('DFS Iterative Inorder: ', end='')
        # Will traverse the entire tree then start from the node at the top of the stack and print nodes until stack is empty
        while True:
            if node != None:
                stack.append(node)
                valueStack.append(node.data)
                if node.right != None:
                    node = node.right
                else:
                    node = node.left
            elif stack:
                node = stack.pop()
                valueStack.pop()
                print(node.data, end=' ')
                node = None
            else:
                break
        print()

    def _dfsHelperPreorder(self, node):
        print(node.data, end=' ')
        if node.left != None:
            self._dfsHelperPreorder(node.left)
        elif node.right != None:
            self._dfsHelperPreorder(node.right)

    def _dfsHelperInorder(self, node):
        if node.left != None:
            self._dfsHelperInorder(node.left)
        print(node.data, end=' ')
        if node.right != None:
            self._dfsHelperInorder(node.right)

    def _dfsHelperPostorder(self, node):
        if node.left != None:
            self._dfsHelperPostorder(node.left)
        elif node.right != None:
            self._dfsHelperPostorder(node.right)
        print(node.data, end=' ')


# Initialize nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.right = node2
node2.left = node3
# node1.dfs('preorder')
# node1.dfs('inorder')
# node1.dfs('postorder')
node1.iterativePreorder()
node1.iterativeInorder()
node1.iterativePostorder()
