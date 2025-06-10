# biblioteca para fila de prioridade
import heapq

def dijkstra(graph, start): # acha as menores distâncias para cada node, não um específico
    # cria um dicionário contendo as menores distâncias até um node
    distances = {node: float('infinity') for node in graph}
    
    # define a distância do node inicial como zero
    distances[start] = 0
    
    # lista dos antecessores
    predecessors = {node: None for node in graph}
    
    # priority queue (distancia, node)
    pq = [(0, start)]
    
    while pq:
        # tira o elemento de maior prioridade
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance < distances[current_node]:
            # se a distância que a achamos for maior que a menor distância encontrada, já pulamos esse 
            
        
            # para cada vizinho
            for neighbor, weight in graph[current_node].items():
                # distancia vai ser distancia atual + peso do caminho percorrido
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    # se o caminho atual for o menor, atualizamos o valor e adicionamos esse node na fila para verificar seus vizinhos
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                
    return distances, predecessors

def get_shortest_path(predecessors, start, target):
    path = []
    current_node = target
    
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    
    if path[0] == start:
        return path
    else:
        return []

# Exemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
target_node = 'D'
distances, predecessors = dijkstra(graph, start_node)
print(distances)
print(predecessors)

shortest_path = get_shortest_path(predecessors, start_node, target_node)
# if shortest_path:
#     print(f"O menor caminho de {start_node} para {target_node} é: {' -> '.join(shortest_path)}")
# else:
#     print(f"Não há caminho de {start_node} para {target_node}")
