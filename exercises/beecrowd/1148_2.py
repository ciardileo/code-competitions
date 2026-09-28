"""
Descobrir o tempo mínimo para enviar uma carta entre vários pares de cidades
Djikstra

4 5
1 2 5
2 1 10
3 4 8
4 3 7
2 3 6
5
1 2
1 3
1 4
4 3
4 1
3 3
1 2 10
2 3 1
3 2 1
3
1 3
3 1
3 2
0 0
"""

from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush
input = lambda: stdin.readline().rstrip()

def dijkstra(grafo, start, alvo):
    # dicionário de distâncias
    distances = {node: float("inf") for node in grafo}
    distances[start] = 0
    # print(grafo)
    # inicia a priority queue
    pq = [(0, start)]

    # print(f"Vou de {start} a {alvo}")

    # enquanto houver uma fila
    while pq:
        atual, node = heappop(pq)
        # print(atual, node)
        # print(distances)
        # print(grafo)
        # se o caminho que encontramos é menor que o menor registrado
        if distances[node] >= atual:
            # print("ok1")
            # para cada vizinho
            for neighbour, weight in grafo[node].items():
                distance = atual + weight

                # se o caminho até esse vizinho for o menor registrado, adiciona na fila
                if distance < distances[neighbour]:
                    # atualiza o menor caminho
                    distances[neighbour] = distance
                    heappush(pq, (distance, neighbour))

    if distances.get(alvo, -1) != float("inf") and distances.get(alvo, -1) != -1:
        return distances[alvo]
    return "Nao e possivel entregar a carta"



def main():
    while True:
        # cidades, acordos (nós, arestas)
        N, E = map(int, input().split())

        # condição de parada
        if N == E == 0:
            break

        # grafo (matriz de adjascência)
        grafo = defaultdict(dict)

        # arestas/acordos
        for _ in range(E):
            # cidade X, cidade Y, horas
            X, Y, H = map(int, input().split())

            # tira um para contar com o índice 0
            X -= 1
            Y -= 1

            # marca o peso no grafo
            if grafo[Y].get(X, -1) != -1:
                grafo[X][Y] = 0
                grafo[Y][X] = 0 
            else:
                grafo[X][Y] = H

        # print(*grafo, sep="\n")
        # consultas
        K = int(input())

        # para cada par de testes
        for _ in range(K):
            O, D = map(int, input().split())
            O -= 1
            D -= 1

            print(dijkstra(grafo, O, D))

        print()


if __name__ == "__main__":
    main()