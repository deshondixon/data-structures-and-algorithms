class LinkedList:
    def __init__(self):
        self.headval = None

    def __str__(self):
        current = self.headval
        result = ""
        while current is not None:
            result += "{{ {0} }} -> ".format(current.dataval)
            current = current.nextval
        result += "NULL"
        return result

    def insert(self, dataval):
        new_node = Node(dataval)
        new_node.nextval = self.headval
        self.headval = new_node

    def includes(self, dataval):
        current = self.headval
        while current is not None:
            if current.dataval == dataval:
                return True
            current = current.nextval
        return False

    def append(self, dataval):
        new_node = Node(dataval)
        if self.headval is None:
            self.headval = new_node
            return
        current = self.headval
        while current.nextval is not None:
            current = current.nextval
        current.nextval = new_node

    def insert_before(self, before, dataval):
        if self.headval is None:
            raise TargetError("List is empty")
        if not self.includes(before):
            raise TargetError("Value not found in list")
        current = self.headval
        previous = None
        while current.dataval != before:
            previous = current
            current = current.nextval
        new_node = Node(dataval)
        new_node.nextval = current
        if previous is not None:
            previous.nextval = new_node
        if previous is None:
            self.headval = new_node

    def insert_after(self, after, value):
        current = self.headval
        try:
            while current.dataval is not after:
                current = current.nextval
            new_node = Node(value)
            new_node.nextval = current.nextval
            current.nextval = new_node
        except Exception as e:
            raise TargetError(e)

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError(Exception)
        current = self.headval
        kth_node = self.headval
        counter = 0
        while current is not None:
            if counter > k:
                kth_node = kth_node.nextval
            current = current.nextval
            counter += 1
        if counter <= k:
            raise TargetError(Exception)
        return kth_node.dataval


class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class TargetError(Exception):
    pass
