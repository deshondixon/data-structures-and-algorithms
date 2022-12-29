class LinkedList:
    def __init__(self):
        # initialization here
        self.headval = None

    def __str__(self):
        # method body here
        printval = self.headval
        string_values = ""
        while printval is not None:
            string_values += f"{{ {str(printval.dataval)} }} -> "
            printval = printval.nextval
        string_values += "NULL"
        return string_values

    def append(self, dataval):
        current = self.headval
        while current.nextval is not None:
            current = current.nextval
        current.nextval = Node(dataval)

    def insert(self, dataval):
        new_node = Node(dataval)
        if self.headval:
            new_node.nextval = self.headval
            self.headval = new_node
        else:
            self.headval = new_node

    def includes(self, dataval):
        current = self.headval
        while current is not None:
            if current.dataval == dataval:
                return True
            current = current.nextval
        return False


    def insert_before(self, before, dataval):
        current = self.headval
        previous = None
        try:
            while current.dataval is not before:
                previous = current
                current = current.nextval
            new_node = Node(dataval)
            new_node.nextval = current
            if previous is not None:
                previous.nextval = new_node
            if previous is None:
                self.headval = new_node
        except Exception as e:
            raise TargetError(e)

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

    def kth_from_end(self, dataval):
        current = self.headval
        length = 0
        while current is not None:
            current = current.nextval
            length += 1
        if dataval >= length:
            raise TargetError(Exception)
        if dataval < 0:
            raise TargetError(Exception)
        current = self.headval
        for x in range(0, length - dataval - 1):
            print(current.dataval)
            current = current.nextval
        return current.dataval

    def append(self, dataval):
        current = self.headval
        if current is not None:
            self.headval = Node(dataval)
        else:
            while current.nextval:
                current = current.nextval
            current.nextval = Node(dataval)
        return False


class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        

class TargetError(Exception):
    pass
