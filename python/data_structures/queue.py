from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, dataval, next=None):
        self.dataval = dataval
        self.next = next


class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, dataval):
        if self.back:
            self.back.next = Node(dataval)
            self.back = self.back.next
            return
        self.back = self.front = Node(dataval)

    def dequeue(self):
        try:
            if self.front == self.back:
                dequeued = self.front
                self.front = self.back = None
                return dequeued.dataval
            dequeued = self.front
            self.front = self.front.next
            return dequeued.dataval
        except Exception as e:
            raise InvalidOperationError(e)

    def peek(self):
        try:
            return self.front.dataval
        except Exception as e:
            raise InvalidOperationError(e)

    def is_empty(self):
        return self.front is None
