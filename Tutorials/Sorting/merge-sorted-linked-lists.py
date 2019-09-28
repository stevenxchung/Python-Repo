'''
Given n sorted linked list, create one sorted linked list
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head
