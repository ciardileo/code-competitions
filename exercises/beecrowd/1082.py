"""
Algoritmo de Warshall
"""

def main():
    N = int(input())

    for case in range(N):
        V, E = map(int, input().split())
        graph = [[0] * V for i in range(V)] 

        for _ in range(E):
            a, b = input().split()
            a, b = ord(a) - 97, ord(b) - 97   # traduz de letra para número
            graph[a][a] = 1
            graph[b][b] = 1
            graph[a][b] = 1
            graph[b][a] = 1


        # fecho transitivo
        for k in range(V):
            for i in range(V):
                if i == k:
                    graph[i][k] = 1

                for j in range(V):

                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1

        # análise dos componenentes conexos
        # print(*graph, sep="\n")
        print(f"Case #{case + 1}:")
        components = set()
        for i in range(V):
            if tuple(graph[i]) not in components:
                components.add(tuple(graph[i]))
                for j in range(V):
                    if graph[i][j] > 0:
                        print(chr(j + 97), end=",")
                
                print()
                
        print(f"{len(components)} connected components\n")




if __name__ == "__main__":
    main()