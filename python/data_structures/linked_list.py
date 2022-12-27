class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


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


class TargetError:
    pass
