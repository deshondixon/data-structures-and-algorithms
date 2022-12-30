# Singly Linked List

[Linked List Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/linked_list.py)

## Challenge
<!-- Description of the challenge -->

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Create a Linked List class

Within your Linked List class, include a head property.

Upon instantiation, an empty Linked List should be created.

The class should contain the following methods

- insert

  - Arguments: value
  - Returns: nothing

Adds a new node with that value to the head of the list with an O(1) Time performance.

- includes

  - Arguments: value
  - Returns: Boolean

Indicates whether that value exists as a Node’s value somewhere within the list.

- to string

  - Arguments: none
  - Returns: a string representing all the values in the Linked List, formatted as:
  "{ a } -> { b } -> { c } -> NULL"

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Any exceptions or errors that come from your code should be contextual, descriptive, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom error that describes what went wrong in calling the methods you wrote for this lab.

Write tests to prove the following functionality:

Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
Ensure your tests are passing before you submit your solution.

## Big O Notation
    - Time is O(1) because the utilizing insert will replace head with node.
    - Space is O(n) because of the amount of space taken up in the  memory will increase because new items added to thr list will be stored there.

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

- Singly linked lists use the Node class to create nodes

- By using the Node class, we add nodes to the LinkedList class

## API

- insert

  - Arguments: value
  - Returns: nothing

- includes

  - Arguments: value
  - Returns: Boolean

- to string

  - Arguments: none
  - Returns: a string representing all the values in the Linked List, formatted as:
  "{ a } -> { b } -> { c } -> NULL"

## Tests

Wrote tests to prove the following functionality:

- Can successfully instantiate an empty linked list
- Can properly insert into the linked list
- The head property will properly point to the first node in the linked list
- Can properly insert multiple nodes into the linked list
- Will return true when finding a value within the linked list that exists
- Will return false when searching for a value in the linked list that does not exist
- Can properly return a collection of all the values that exist in the linked list.

## References
Used the following references to help complete code challenge:
- https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
- https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html
- https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d
- https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996
