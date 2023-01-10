from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    result = []
    if not tree.root:
        return result
    queue = [tree.root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
