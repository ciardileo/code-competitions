"""
meter um warshall e verificar se cada grafo é composto de um único componente conexo 
fim da entrada é 00

4 5
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
3 2
1 2 2
1 3 2
3 2
1 2 2
1 3 1
4 2
1 2 2
3 4 2
0 0
"""

from sys import stdin
from collections import defaultdict, deque

input = lambda: stdin.readline().rstrip()

def bfs(grafo, N):
    visited = set(("1"))
    queue = deque(("1"))

    while queue:
        node = queue.popleft()
        # print(node)

        for neighbour in grafo[node] - visited:
            visited.add(neighbour)
            queue.append(neighbour)

    if len(visited) == N:
        return 1
    else: 
        return 0



def main():
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break

        grafo = defaultdict(set)
        transposto = defaultdict(set)

        for _ in range(M):
            V, W, P = input().split()

            grafo[V].add(W)
            transposto[W].add(V)

            if P == "2":
                grafo[W].add(V)
                transposto[V].add(W)

        # print(list(grafo.items()))
        if bfs(grafo, N) == bfs(transposto, N) == 1:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()