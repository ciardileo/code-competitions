"""
graph adjacency list
"""

# dictionary > set representation
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'F'},
    'C': {'A', 'F'},
    'D': {'B',},
    'E': {'B', 'F'},
    'F': {'C', 'E'}         
}


# classe para cada node
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    
    # inicia a lista
    def __init__(self, num):
        self.vertices = num
        self.graph = [None] * self.vertices

    # add edges
    def add_edge(self, v1, v2):
        node = AdjNode(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node

        node = AdjNode(v1)
        node.next = self.graph[v2]
        self.graph[v1] = node

    # print the graph
    def display(self):
        for i in range(self.vertices):
            print(f'Vertex {i}: ', end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.display()