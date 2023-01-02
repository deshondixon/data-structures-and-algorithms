# Stacks and Queues

[Stack Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/stack.py)

[Queue Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/stack.py)

## Challenge
<!-- Description of the challenge -->

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Whiteboard Process
<!-- Embedded whiteboard image -->

![coming soon...](./White Board.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available to your Stack and Queue-->

### Stack

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

### Queue

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
