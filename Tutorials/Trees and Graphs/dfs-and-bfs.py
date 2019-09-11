class Node(object):
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

    def dfs(self):
        print('DFS Recursive: ', end='')
        self._dfsHelper(self)
        print()

    def _dfsHelper(self, node):
        print(node.data, end=' ')
        if node.children != None:
            for child in node.children:
                self._dfsHelper(child)

    def dfsIterative(self):
        stack = []
        stack.append(self)
        print('DFS Iterative: ', end='')
        while len(stack) > 0:
            node = stack.pop()
            print(node.data, end=' ')
            if node.children != None:
                stack += reversed(node.children)
        print()

    def bfs(self):
        queue = []
        queue.append(self)
        print('BFS: ', end='')
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.children != None:
                for child in node.children:
                    queue.append(child)
        print()


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.children = [b, c, d]
b.children = [e, f]
a.dfs()
a.dfsIterative()
a.bfs()
