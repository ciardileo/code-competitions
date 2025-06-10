"""
dada as configurações das pontes, determinar o número mínimo de buracos que pedrinho terá que pular para chegar do outro lado
0 é onde pedrinho está
de 1 a N estão os pilares
N + 1 é o final
"""

from collections import defaultdict
import heapq

def main():
    def dijkstra(graph, start):
        # criar o dicionário de menor distância de cada node ao inicio
        distances = {node: float('inf') for node in graph}
        
        # inicializa a distância do inicial como zero
        distances[start] = 0
        
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # se a distância que encontramos nesse caminho for maior que a menor distância, ignoramos o resto
            if current_distance > distances[current_node]:
                continue
            
            # para cada vizinho do node atual
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                # se a distância pelo novo caminho for menor que a menor conhecida, atualizamos ela
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
        return distances
    
    nodes, pontes = [int(x) for x in input().split()]
    grafo = defaultdict(list)
    
    
    for _ in range(pontes):
        try:
            pilar1, pilar2, buracos = [int(x) for x in input().split()]
        except:
            pass
        finally:
            grafo[pilar1].append((pilar2, buracos))
            grafo[pilar2].append((pilar1, buracos))
        
    print(dijkstra(grafo, 0)[nodes + 1])
        
    
    
if __name__ == "__main__":
    main()
