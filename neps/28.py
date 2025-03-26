"""
N cidades de 1 a N
Inicio: 1
Destino: N
djikstra para achar o menor caminho entre 1 e N
"""

import heapq
from collections import defaultdict

def main():
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        
        queue = [(0, 1),]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
                    
        return distances
    
    cidades, pares = [int(x) for x in input().split()]
    mapa = defaultdict(list)
    
    for _ in range(pares):
        cidade1, cidade2, peso = [int(x) for x in input().split()]
        mapa[cidade1].append((cidade2, peso))
        mapa[cidade2].append((cidade1, peso))
        
    print(dijkstra(mapa, 1)[cidades])
    
    
if __name__ == "__main__":
    main()