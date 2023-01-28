# Hash Tables

[Hash Table Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/hashtable.py)

## Challenge
<!-- Description of the challenge -->

- Implement a Hashtable Class
- Utilize the Single-responsibility principle:
  - any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

- Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

- Any exceptions or errors that come from your code should be contextual, descriptive, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom error that describes what went wrong in calling the methods you wrote for this lab.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Hash Table](./White_Board.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O Notation:

- time -  -
- space -  -

## API
<!-- Description of each method publicly available to your Stack and Queue-->

- set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.

- get
  - Arguments: key
  - Returns: Value associated with that key in the table

- has
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.

- keys
  - Returns: Collection of keys

- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Tests

[Hash Table Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_hashtable.py)

## References

-
