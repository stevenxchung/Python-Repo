from time import time


class UnionFind:
    def __init__(self, n: int, debug=False):
        self.debug = debug
        self.parent = [n for n in range(n)]
        self.rank = [1] * n

    def find(self, x: int, isInternal=False) -> int:
        '''
        Return the root of the component that x belongs to.
        '''
        p = x
        while p != self.parent[p]:
            # Path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        if self.debug and not isInternal:
            return print(f'find({x}): {p}')
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        '''
        Return whether x and y belong to the same component.
        '''
        p1, p2 = self.find(x, isInternal=True), self.find(y, isInternal=True)

        res = p1 == p2
        if self.debug:
            return print(f'isSameComponent({res}): {res}')
        return res

    def union(self, x: int, y: int) -> bool:
        '''
        Union the components that x and y belong to.
        If they are already in the same component, return false, otherwise return true.
        '''
        p1, p2 = self.find(x, isInternal=True), self.find(y, isInternal=True)

        if p1 == p2:
            if self.debug:
                return print(f'union({x}, {y}): {False}')
            return False
        elif self.rank[p2] > self.rank[p1]:
            # When p2's rank is greater than p1's rank
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            # Otherwise, go with p1 as parent
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        if self.debug:
            return print(f'union({x}, {y}): {True}')

        return True

    def getNumComponents(self) -> int:
        '''
        Return the number of components in the disjoint set.
        '''
        res = len(set(self.parent))
        if self.debug:
            return print(f'getNumComponents(): {res}')
        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = UnionFind(10, debug=True)
    test.find(1)
    test.isSameComponent(1, 3)
    test.union(1, 2)
    test.union(2, 3)
    test.getNumComponents()
    test.isSameComponent(1, 3)

    print('\nAdditional testing...')
    test = UnionFind(4, debug=True)
    test.union(0, 1)
    test.union(2, 3)
    test.find(0)
    test.find(2)

    print(f'Runtime for our solution: {time() - sol_start}\n')
