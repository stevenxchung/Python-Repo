from time import time


class DynamicArray:
    def __init__(self, capacity: int, debug=False):
        self.debug = debug
        self.capacity = capacity
        self.arr = []

    def get(self, i: int) -> int:
        '''
        Return the element at index i.
        '''
        if i < len(self.arr):
            res = self.arr[i]
            if self.debug:
                print(f'arr[{i}]: {res}')
            return res

    def set(self, i: int, n: int) -> None:
        '''
        Set the element at index i to n.
        '''
        if i < len(self.arr):
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        '''
        Push the element n to the end of the array.
        If the array is full, resize the array first.
        '''
        if len(self.arr) + 1 > self.capacity:
            self.resize()
        self.arr.append(n)

    def popback(self) -> int:
        '''
        Pop and return the element at the end of the array.
        '''
        if len(self.arr) > 0:
            res = self.arr.pop()
            if self.debug:
                print(f'Pop back the last element: {res}')
            return res

    def resize(self) -> None:
        '''
        Double the capacity of the array.
        '''
        self.capacity *= 2

    def getSize(self) -> int:
        '''
        Return the number of elements in the array.
        '''
        res = len(self.arr)
        if self.debug:
            print(f'Number of elements in array: {res}')
        return res

    def getCapacity(self) -> int:
        '''
        Return the capacity of the array.
        '''
        res = self.capacity
        if self.debug:
            print(f'Max capacity of the array: {res}')
        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = DynamicArray(1, debug=True)
    test.getSize()  # 0
    test.getCapacity()  # 1

    print('\n##### Test 2 #####')
    test = DynamicArray(1, debug=True)
    test.pushback(1)
    test.getCapacity()  # 1
    test.pushback(2)
    test.getCapacity()  # 2

    print('\n##### Test 3 #####')
    test = DynamicArray(1, debug=True)
    test.getSize()  # 0
    test.getCapacity()  # 1
    test.pushback(1)
    test.getSize()  # 1
    test.getCapacity()  # 1
    test.pushback(2)
    test.getSize()  # 2
    test.getCapacity()  # 2
    test.get(1)  # 2
    test.set(1, 3)
    test.get(1)  # 3
    test.popback()  # 3
    test.getSize()  # 1
    test.getCapacity()  # 2

    print(f'Runtime for our solution: {time() - sol_start}\n')
