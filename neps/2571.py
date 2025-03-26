"""
montar o grafo com as conexões e o peso delas (entre a mesma estação o peso é 0)
aplicar um djikstra depois que o grafo estiver montado
"""

from collections import defaultdict
import heapq

def main():
    def djikstra(graph, start):
        distances = {node: float("inf") for node in range(1, N + 1)}
        
        distances[start] = 0
        k
        # sistema, distancia atual, node inicial
        pq = [(-1, 0, start)]
        
        while pq:
            current_system, current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances[current_node]:
                continue
                
            for neighbor, system in graph[current_node]:
                new_distance = current_distance
                if system != current_system:
                    new_distance = current_distance + passagens[system]
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (system, new_distance, neighbor))
                        
        return distances

    
    N, M, K = [int(x) for x in input().split()]  # estações, ligações, sistemas
    
    passagens = [int(x) for x in input().split()]
    grafo = defaultdict(list)
    
    for _ in range(M):
        v, u, t = [int(x) for x in input().split()]  # estacao 1, estacao 2, sistema
        
        # adiciona a conexão no grafo
        grafo[v].append((u, t - 1))
        grafo[u].append((v, t - 1))
        
    a, b = [int(x) for x in input().split()]  # estação inicial e final
    
    resultado = djikstra(grafo, a)
    print(resultado[b] if resultado[b] != float('inf') else -1)
        
    
    
    
    
if __name__ == "__main__":
    main()