# Binary Tree and BST Implementation

[Binary Tree Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/binary_tree.py)

[Binary Search Tree Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/binary_search_tree.py)
## Challenge
<!-- Description of the challenge -->

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Create a Binary Tree class.

Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class.



## Whiteboard Process
<!-- Embedded whiteboard image -->

No whiteboard required

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O Notation:

- time -
- space -

## API
<!-- Description of each method publicly available to your Stack and Queue-->

#### Binary Tree

- Define a method for each of the depth first traversals:
   - pre order
   - in order
   - post order

#### Binary Search Tree

- Add
  - Arguments: value
  - Return: nothing
  - Adds a new node with that value in the correct location in the binary search tree.


- Contains
  - Argument: value
  - Returns: boolean indicating whether the value is in the tree at least once.

## Tests

[Binary Tree Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_binary_tree.py)

[Binary Search Tree Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_binary_search_tree.py)

Wrote tests to prove the following functionality:

- Can successfully instantiate an empty tree

- Can successfully instantiate a tree with a single root node

- For a Binary Search Tree, can successfully add a left child and right child properly to a node

- Can successfully return a collection from a preorder traversal

- Can successfully return a collection from an inorder traversal

- Can successfully return a collection from a postorder traversal

- Returns true	false for the contains method, given an existing or non-existing node value


## Solution

#### Binary Tree

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


    class BinaryTree:
        def __init__(self):
            self.root = None

        def post_order(self, root=None, nodes=None):
            """
            Return a list of nodes in a BT, in postorder
            eg: [4, 5, 2, 6, 7, 3, 1]
            """
            # Start at the root of our tree
            if root is None:
                root = self.root

            # First time method is invoked
            if nodes is None:
                nodes = []

            # Left child
            if root.left:
                self.post_order(root.left, nodes)

            # Right child
            if root.right:
                self.post_order(root.right, nodes)

            # Root
            nodes.append(root.value)

            print(nodes)
            # Base Case
            return nodes

        def pre_order(self, root=None, nodes=None):
            """
            Return a list of nodes in a BT, in preorder
            eg: ["a", "b", "d", "e", "c", "f", "g"]
            """
            # Start at the root of our tree
            if root is None:
                root = self.root

            # First time method is invoked
            if nodes is None:
                nodes = []

            # Root
            nodes.append(root.value)

            # Left child
            if root.left:
                self.pre_order(root.left, nodes)

            # Right child
            if root.right:
                self.pre_order(root.right, nodes)

            print(nodes)
            # Base Case
            return nodes

        def in_order(self, root=None, nodes=None):
            """
            Return a list of nodes in a BT, in inorder
            eg: ["d", "b", "e", "a", "f", "c", "g"]
            """
            # Start at the root of our tree
            if root is None:
                root = self.root

            # First time method is invoked
            if nodes is None:
                nodes = []

            # Left child
            if root.left:
                self.in_order(root.left, nodes)

            # Root
            nodes.append(root.value)

            # Right child
            if root.right:
                self.in_order(root.right, nodes)

            print(nodes)
            # Base Case
            return nodes

#### Binary Search Tree

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


## Reference

Used Adam's example from class to complete this challenge.
