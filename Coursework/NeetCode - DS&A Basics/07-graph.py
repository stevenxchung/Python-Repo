from collections import defaultdict
from time import time


class Graph:
    def __init__(self, debug=False):
        self.debug = debug
        self.node_map = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        '''
        Add an edge from src to dst if it does not already exist.
        If either src or dst do not exist, add them to the graph.
        '''
        self.node_map[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        '''
        Remove the edge from src to dst if it exists.
        Return whether the edge was removed.
        Either src or dst may not exist in the graph.
        '''
        if src in self.node_map and dst in self.node_map[src]:
            self.node_map[src].remove(dst)
            if self.debug:
                print(f'removeEdge({src}, {dst}): {True}')
            return True

        if self.debug:
            print(f'removeEdge({src}, {dst}): {False}')
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        '''
        Return whether there is a path from src to dst.
        Assume both src and dst exist in the graph.
        '''

        def dfs(node):
            if node == dst:
                return True
            if node not in self.node_map:
                return False

            for nei in self.node_map[node]:
                if dfs(nei):
                    return True

            return False

        res = dfs(src)
        if self.debug:
            print(f'hasPath({src}, {dst}): {res}')

        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = Graph(debug=True)
    test.addEdge(1, 2)
    test.addEdge(2, 3)
    test.hasPath(1, 3)
    test.hasPath(3, 1)
    test.removeEdge(1, 2)
    test.hasPath(1, 3)

    print('\n##### Test 2 #####')
    test = Graph(debug=True)
    test.addEdge(1, 2)
    test.addEdge(2, 3)
    test.addEdge(3, 1)
    test.hasPath(1, 3)
    test.hasPath(3, 1)

    print(f'Runtime for our solution: {time() - sol_start}\n')
