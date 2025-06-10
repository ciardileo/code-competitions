"""
em uma mina, calcular qual é o caminho com menor peso até o final dela
passagens normais tem peso 0 
passagens com pedra tem peso 1
"""

import heapq

def main():
    def dijkstra(graph, x, y):
        # inicializar a matrix de distâncias
        distances = [[float('inf')] * N for _ in range(N)]
        distances[0][0] = 0
        
        # cria a fila de prioridade (distancia atual do zero, x, y)
        # a fila de prioridade é utilizada pois se enquanto estivermos percorrendo o grafo, acharmos um caminho até o node A, menor do que já estava registrado na fila, este vai ser priorizado, e quando o outro for ser processado, ele cairá no continue do if
        queue = [(0, x, y)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            current_distance, current_row, current_col = heapq.heappop(queue)
            
            # se ja foi encontrado um caminho mais eficiente que esse, passar para o próximo. Isso evita a repetição de um mesmo node
            if current_distance > distances[current_row][current_col]:
                continue
            
           
            # para cada vizinho
            for hor, ver in directions:
                new_row, new_col = hor + current_row, ver + current_col
                
                # se estiver dentro dos limites
                if 0 <= new_row < N and 0 <= new_col < N:
                    # a nova distância até o 0 vai ser a distância até o node atual + peso do caminho atual
                    new_distance = current_distance + graph[new_row][new_col]
                    
                    # se a distância encontrada por esse caminho for menor que a menor distância encontrada ate agora, vamos atualizar ela e mandar para a fila como o caminho com menor distãncia
                    if new_distance < distances[new_row][new_col]:
                        distances[new_row][new_col] = new_distance
                        heapq.heappush(queue, (new_distance, new_row, new_col))
                        
        return distances
    
    N = int(input())  # dimensões da mina
    mina = []
    
    # cria o mapa da mina
    for _ in range(N):
        mina.append([int(x) for x in input().split()])
        
    print(dijkstra(mina, 0, 0)[N-1][N-1])
    
if __name__ == '__main__':
    main()