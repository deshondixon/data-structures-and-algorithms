# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")

  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute. Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`

## Table of Contents

- [Array Reverse](docs/array_reverse/README.md)
- [Array Insert Shift](docs/array_insert_shift/README.md)
- [Array Binary Search](docs/array_binary_search/README.md)
- [Linked List](docs/linked_list/README.md)
- [Linked List Insertions](docs/linked_list_insertions/README.md)
- [Linked List KTH](docs/linked_list_kth/README.md)
- [Linked List ZIP](docs/linked_list_zip/README.md)
- [Stack and Queue](docs/stack_and_queue/README.md)
- [Stack and Queue Pseudo](docs/stack_queue_pseudo/README.md)
- [Stack and Queue Animal Shelter](docs/stack_queue_animal_shelter/README.md)
- [Stack and Queue Brackets](docs/stack_queue_brackets/README.md)
- [Binary Tree and BST Implementation](docs/trees/README.md)
- [Tree Max](docs/tree_max/README.md)
- [Tree Breadth First](docs/tree_breadth_first/README.md)
- [Tree Fizz Buzz](docs/tree_fizz_buzz/README.md)
- [Insertion Sort](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/sorting/insertion/README.md)
- [Merge Sort](https://github.com/deshondixon/data-structures-and-algorithms/tree/main/sorting/merge/README.md)
- [Sort Comparison](https://github.com/deshondixon/data-structures-and-algorithms/tree/main/sorting/sort/README.md)
- [Hash Table](docs/hashtable/README.md)
- [HashTable Repeated Table](docs/hashtable_repeated_word/README.md)
- [Tree Intersection](docs/tree_intersection/README.md)
- [Graph](docs/graph/README.md)
- [Graph Business Trip](docs/graph_business_trip/README.md)
- [Graph Depth First Traversal](docs/graph_depth_first/README.md)
