'''
Implement a Queue() with methods add(), get_item(), and is_empty()
'''


class DoubleLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head, self.tail = DoubleLLNode(), DoubleLLNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.tail.prev = self.head

    def add(self, val: int):
        print("Adding item to queue")
        node = DoubleLLNode(val)
        if self.size == 0:
            self.head.next, self.tail.prev = node, node
            node.prev, node.next = self.head, self.tail
        else:
            first_node = self.head.next
            self.head.next, first_node.prev = node, node
            node.prev, node.next = self.head, first_node
        self.size += 1

    def get_item(self) -> int:
        print("Getting item from queue")
        last_node = self.tail.prev
        self.tail.prev = last_node.prev
        self.size -= 1
        return last_node.val

    def is_empty(self) -> bool:
        return self.size == 0


print("Queue implementation")


test = Queue()
test.add(1)
test.add(2)
test.add(3)
print(test.get_item())  # 1
print(test.is_empty())  # false, two items exists

print(test.get_item())  # 2
print(test.get_item())  # 3
print(test.is_empty())  # true, no items exists
