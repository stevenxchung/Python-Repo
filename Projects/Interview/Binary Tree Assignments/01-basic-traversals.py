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
node1.dfs('preorder')
node1.dfs('inorder')
node1.dfs('postorder')
