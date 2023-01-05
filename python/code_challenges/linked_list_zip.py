from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    result = LinkedList()
    a_node = a.headval
    b_node = b.headval
    while a_node is not None or b_node is not None:
        if a_node is not None:
            result.append(a_node.dataval)
            a_node = a_node.nextval
        if b_node is not None:
            result.append(b_node.dataval)
            b_node = b_node.nextval
    return result
