"""
dfs and bfs in graphs
"""

# graph in adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'F'},
    'C': {'A', 'F'},
    'D': {'B',},
    'E': {'B', 'F'},
    'F': {'C', 'E'}         
}

# DFS algorithm
def dfs(graph, start, visited=None):
    # cria o set dos visitados caso não tenha sido criado
    if visited is None:
        visited = set()
        
    visited.add(start)

    print(start)

    # para cada node adjascente que não tenha sido visitado ainda (graph[start] - visited)
    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited

visited_dfs = dfs(graph, 'A')
print(visited_dfs)

print('-=' * 25)

# BFS algorithm
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
        print()
        
    return visited
        
visited_bfs = bfs(graph, 'A')
print(visited_bfs)