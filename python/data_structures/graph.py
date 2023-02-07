class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight


class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.vertices = {}

    def add_node(self, value):
        node = Vertex(value)
        self.vertices[node] = []
        return node

    def add_edge(self, start, end, weight=None):
        self.vertices[start].append(Edge(end, weight))
        self.vertices[end].append(Edge(start, weight))

    def get_nodes(self):
        return list(self.vertices.keys())

    def get_neighbors(self, node):
        return self.vertices[node]

    def size(self):
        return len(self.vertices)

    def get_flight(self, start, end, path=None, visited=None):
        """
        This method returns the shortest weight path between two nodes.
        """
        if path is None:
            path = []
        if visited is None:
            visited = []

        start_vertex = self.vertices.get(start)
        if start_vertex is None:
            return None

        if start in visited:
            return None

        visited.append(start)
        if start == end:
            return path

        shortest_path = None
        for edge in start_vertex:
            if edge.vertex not in visited:
                new_path = path + [edge.vertex.value]
                trip = self.get_flight(edge.vertex, end, new_path, visited)
                if trip is not None:
                    if shortest_path is None or len(trip) < len(shortest_path):
                        shortest_path = trip

        return shortest_path


class Vertex:
    def __init__(self, value):
        self.value = value
        self.dataval = value


def get_flight(self, start, end):
    if start not in self.vertices or end not in self.vertices:
        return None
    queue = [start]
    visited = {vertex: False for vertex in self.vertices}
    visited[start] = True
    while queue:
        current = queue.pop(0)
        for neighbor in self.get_neighbors(current):
            if neighbor.vertex == end:
                return current, neighbor.vertex, neighbor.weight
            if not visited[neighbor.vertex]:
                visited[neighbor.vertex] = True
                queue.append(neighbor.vertex)
    return None
