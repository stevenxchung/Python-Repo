class Node(object):
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.children = [b, c, d]
b.children = [e, f]
