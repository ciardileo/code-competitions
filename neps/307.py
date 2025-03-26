"""
imprimir a distância entre a cozinha e a sala mais distante, considerando que a cozinha está no lugar onde essa distância é mínima
fazer um dijkstra em todos os comodos e retornar qual é a maior distância da lista de menores
depois de fazer de todos, mostrar a menor distância entre todas
"""

from collections import defaultdict
import heapq

def main():
    def dijkstra(graph, start):
        distances = [float('inf') for node in graph]
        distances[start - 1] = 0
        
        queue = [(0, start),]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node - 1]:
                continue
            
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight
                
                if new_distance < distances[neighbor - 1]:
                    distances[neighbor - 1] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
                    
        return distances
    
    salas, corredores = [int(x) for x in input().split()]
    grafo = defaultdict(list)
    
    for _ in range(corredores):
        sala1, sala2, peso = [int(x) for x in input().split()]
        
        grafo[sala1].append((sala2, peso))
        grafo[sala2].append((sala1, peso))
        
    resultados = []
    for i in range(1, salas + 1):
        resultados.append(max(dijkstra(grafo, i)))
        
    print(min(resultados))
    
    
if __name__ == "__main__":
    main()