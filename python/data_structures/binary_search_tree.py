from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Subclass of BinaryTree
    """

    def __init__(self):
        self.root = None

    def contains(self, value):
        def walk(value, root):

            if not root:
                return False

            return (
                root.value == value or walk(value, root.left) or walk(value, root.right)
            )

        return walk(value, self.root)

    def add(self, value):
        # check for empty BST
        if self.root is None:
            self.root = Node(value)
            return

        # start pointer at root
        current = self.root

        while current:
            # if number of the added node is less than current node, check left
            if value < current.value:
                # add node only if there's space
                if current.left is None:
                    current.left = Node(value)
                    return

                # if there's no space go left
                current = current.left

            # if number of the added node is greater than current node, check right
            else:
                # add node only if there's space
                if current.right is None:
                    current.right = Node(value)
                    return

                # if there's no space go right
                current = current.right
