# Stacks and Queues

[Stack Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/stack.py)

[Queue Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/stack.py)

## Challenge
<!-- Description of the challenge -->

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.

Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.

## Whiteboard Process
<!-- Embedded whiteboard image -->

- Did not ask for whiteboard on this assignment.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O Notation:
#### Stack
- time O(1) - because the time to complete these methods is not affected by the stack size.
- space O(1) - because the amount of nodes is unaffected by the stack size.

#### Queue
- time O(1) - because the size of the queue does not affect codes execution time.
- space O(1) - because the amount of nodes in queue does not affect the space of the queue.

## API
<!-- Description of each method publicly available to your Stack and Queue-->

#### Stack

push
- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.
-
pop
- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack
- Should raise exception when called on empty stack

peek
- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack

is empty
- Arguments: none
- Returns: Boolean indicating whether the stack is empty.

#### Queue

enqueue
- Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

dequeue
- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue
- Should raise exception when called on empty queue

peek
- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack
is empty
- Arguments: none
- Returns: Boolean indicating whether the queue is empty
## Tests

[Stack List Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_stack.py)

[Queue List Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_queue.py)

Wrote tests to prove the following functionality:

- Can successfully push onto a stack
- Can successfully push multiple values onto a stack
- Can successfully pop off the stack
- Can successfully empty a stack after multiple pops
- Can successfully peek the next item on the stack
- Can successfully instantiate an empty stack
- Calling pop or peek on empty stack raises exception
- Can successfully enqueue into a queue
- Can successfully enqueue multiple values into a queue
- Can successfully dequeue out of a queue the expected value
- Can successfully peek into a queue, seeing the expected value
- Can successfully empty a queue after multiple dequeues
- Can successfully instantiate an empty queue
- Calling dequeue or peek on empty queue raises exception

## Solution

### Stack

    class Node:
        def __init__(self, dataval, next=None):
            self.dataval = dataval
            self.next = next


    class Stack:
        def __init__(self):
            self.top = None

        def push(self, dataval):
            new_node = Node(dataval)
            new_node.next = self.top
            self.top = new_node

        def pop(self):
            if self.top is None:
                raise InvalidOperationError("Method not allowed on empty collection")
            dataval = self.top.dataval
            self.top = self.top.next
            return dataval

        def peek(self):
            if self.top is None:
                raise InvalidOperationError("Method not allowed on empty collection")
            return self.top.dataval

        def is_empty(self):
            return self.top is None

### Queue

    class Node:
        def __init__(self, dataval):
            self.dataval = dataval
            self.next = None


    class Queue:

        def __init__(self):
            self.front = None
            self.back = None

        def enqueue(self, dataval):
            new_node = Node(dataval)
            if self.back:
                self.back.next = new_node
                self.back = new_node
            else:
                self.front = self.back = new_node

        def dequeue(self):
            if self.front is None:
                raise InvalidOperationError
            dequeued = self.front
            self.front = self.front.next
            if self.front is None:
                self.back = None
            return dequeued.dataval

        def peek(self):
            if self.front is None:
                raise InvalidOperationError
            return self.front.dataval

        def is_empty(self):
            return self.front is None
