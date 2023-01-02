class Node:
    def __init__(self, value, next_val=None):
        self.value = value
        self.next = next_val


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
            return self.top.value

    def is_empty(self):
        return self.top is None
