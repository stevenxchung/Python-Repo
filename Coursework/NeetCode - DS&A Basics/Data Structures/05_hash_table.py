from time import time


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=2, debug=False):
        self.debug = debug
        self.capacity = capacity
        self.key_count = 0
        self.nodes = [None] * capacity

    def _get_hashed_index(self, key: int) -> int:
        '''
        Helper function to generate a hash index based on given key and table size.
        '''
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        '''
        Upserts the key-value pair into the hash table.
        '''
        i = self._get_hashed_index(key)
        node = self.nodes[i]

        if not node:
            # Key does not exist
            self.nodes[i] = Node(key, value)
            self.key_count += 1
        else:
            # Either update value if key matches or append to linked list
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next

            prev.next = Node(key, value)
            self.key_count += 1

        if self.key_count / self.capacity >= 0.5:
            # Resize when load factor >= 0.5
            self.resize()

    def get(self, key: int) -> int:
        '''
        Returns the value associated with the key.
        '''
        i = self._get_hashed_index(key)
        node = self.nodes[i]

        while node:
            if node.key == key:
                if self.debug:
                    print(f'get({key}): {node.value}')
                return node.value
            node = node.next

        if self.debug:
            print(f'get({key}): {-1}')
        return -1

    def remove(self, key: int) -> bool:
        '''
        Removes the key-value pair if key is present.
        '''
        i = self._get_hashed_index(key)
        node = self.nodes[i]

        prev = None
        while node:
            if node.key == key:
                if prev:
                    # Remove node from linked list
                    prev.next = node.next
                else:
                    # Remove from beginning of linked list
                    self.nodes[i] = node.next

                self.key_count -= 1
                if self.debug:
                    print(f'remove({key}): {True}')
                return True
            prev, node = node, node.next

        if self.debug:
            print(f'remove({key}): {False}')
        return False

    def getSize(self) -> int:
        '''
        Returns the number of keys in the hash table.
        '''
        res = self.key_count
        if self.debug:
            print(f'getSize(): {res}')
        return res

    def getCapacity(self) -> int:
        '''
        Returns the capacity of the hash table.
        '''
        res = self.capacity
        if self.debug:
            print(f'getCapacity(): {res}')
        return res

    def resize(self) -> None:
        '''
        Doubles the capacity of the hash table.
        '''
        self.capacity *= 2
        new_nodes = [None] * self.capacity

        # For each node or linked list rehash values to a new index
        for node in self.nodes:
            while node:
                i = self._get_hashed_index(node.key)
                if new_nodes[i] is None:
                    # Move node to new index
                    new_nodes[i] = Node(node.key, node.value)
                else:
                    # Move node to end of linked list
                    new_node = new_nodes[i]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)

                node = node.next

        # Assign to new node
        self.nodes = new_nodes


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = HashTable(capacity=4, debug=True)
    test.insert(1, 2)
    test.get(1)
    test.insert(1, 3)
    test.get(1)
    test.remove(1)
    test.get(1)

    print('\n##### Test 2 #####')
    test = HashTable(capacity=2, debug=True)
    test.getCapacity()
    test.insert(6, 7)
    test.getCapacity()
    test.insert(1, 2)
    test.getCapacity()
    test.insert(3, 4)
    test.getCapacity()
    test.getSize()

    print('\nAdditional testing...')
    test = HashTable(capacity=2, debug=True)
    test.insert(7, 7)
    test.insert(8, 8)
    test.insert(9, 9)
    test.getCapacity()
    test.getSize()

    print(f'Runtime for our solution: {time() - sol_start}\n')
