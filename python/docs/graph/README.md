# Graph Implementation

[Graph Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/data_structures/graph.py)

## Challenge
<!-- Description of the challenge -->

- Implement your own Graph. The graph should be represented as an adjacency list.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Graph](./White_Board.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O Notation:

- time -  -
- space -  -

## API
<!-- Description of each method publicly available to your Stack and Queue-->

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph

- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph

- get nodes
  - Arguments: none
  - Returns all the nodes in the graph as a collection (set, list, or similar)
  - Empty collection returned if there are no nodes

- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
    - Include the weight of the connection in the returned collection
  - Empty collection returned if there are no nodes

- size
  - Arguments: none
  - Returns the total number of nodes in the graph
  - 0 if there are none

## Tests

[Graph Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/data_structures/test_graph.py)

## References
