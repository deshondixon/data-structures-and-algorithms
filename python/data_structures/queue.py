from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, dataval):
        new_node = Node(dataval)
        if self.back:
            self.back.next = new_node
            self.back = new_node
        else:
            self.front = self.back = new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        dequeued = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return dequeued.dataval

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        return self.front.dataval

    def is_empty(self):
        return self.front is None
