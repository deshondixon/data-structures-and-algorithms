from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, dataval, next=None):
        self.dataval = dataval
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, dataval):
        new_node = Node(dataval)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        dataval = self.top.dataval
        self.top = self.top.next
        return dataval

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.dataval

    def is_empty(self):
        return self.top is None
