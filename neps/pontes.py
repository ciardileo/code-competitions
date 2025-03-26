"""
ex da OBI 2009 - Primeira Fase
descobrir o menor número de buracos que ele precisa pular para chegar 
0 é o começo
vertices + 1 é o final
"""

import heapq

vertices, edges = [int(x) for x in input().split()]

graph = {v: {} for v in range(vertices + 2)}

for _ in range(edges):
    x, y, weight = [int(x) for x in input().split()]
            
    # peso da aresta que liga x e y
    graph[x][y] = weight
    graph[y][x] = weight
    

def dijkstra(graph, start=0):
    # dict das menores distancias
    distances = {node: float('inf') for node in graph}
    
    distances[0] = 0
    
    # inicia a fila
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))
                    
    return distances

distances = dijkstra(graph)
print(distances[vertices + 1])
    