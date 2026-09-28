"""
Descobrir o tempo mínimo para enviar uma carta entre vários pares de cidades
Floyd-warshall

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
input = lambda: stdin.readline().rstrip()

def main():
    count = 1
    while True:
        # cidades, acordos (nós, arestas)
        N, E = map(int, input().split())

        # condição de parada
        if N == E == 0:
            break

        # grafo (matriz de adjascência)
        grafo = [[float("inf") for _ in range(N)] for _ in range(N)]

        # preencher a diagonal principal com zero
        for i in range(N):
            grafo[i][i] = 0

        # arestas/acordos
        for _ in range(E):
            # cidade X, cidade Y, horas
            X, Y, H = map(int, input().split())

            # tira um para contar com o índice 0
            X -= 1
            Y -= 1

            # marca o peso no grafo
            if grafo[Y][X] != float("inf"):
                grafo[X][Y] = 0
                grafo[Y][X] = 0 
            else:
                grafo[X][Y] = H

        # print(*grafo, sep="\n")
        # Floyd-Warshall O(V^3)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])

        # print(*grafo, sep="\n")
        # consultas
        K = int(input())

        # espaçamento
        if count > 1:
            print()

        # para cada par de testes
        for _ in range(K):
            O, D = map(int, input().split())
            O -= 1
            D -= 1

            # só printa se houver caminho
            if grafo[O][D] != float("inf"):
                print(grafo[O][D])
            else:
                print("Nao e possivel entregar a carta")

        count += 1


if __name__ == "__main__":
    main()