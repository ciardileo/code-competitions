"""
find the number of provincies
the number of provincies is the number of separate graphs in the matrix
n cities
n x n matrix
[i][j] == 1 -> adjascência de duas cidades

passos:
- transformar a matrix em uma lista de adjascência das cidades:
    para cada linha da matrix, criar uma chave com um set vazio, para cada item da linha, adicioná-lo ao set, contanto que i (linha) != j (coluna), para não adicionar a própria cidade em sua lista de conectados
    [       C1  C2 C3
            [1, 1, 0] C1
            [1, 1, 0] C2
            [0, 0, 1] C3
        ]
- para cada cidade, fazer um bfs adicionando cidades visitadas em um set
- repetir o bfs para cada cidade ainda não visitada
- o número de vezes que o bfs foi feito será o número de províncias
"""

# imports
from collections import deque


class Solution:    
    
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # convert the matrix to adjacency list
        graph = {}
        for i in range(len(isConnected)):
            graph[i] = set()
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    graph[i].add(j)
                    
        # bfs function         
        def bfs(graph, start):
            # initializing the variables
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                visited.add(node)
                
                for neigbour in graph[node] - visited:
                    queue.append(neigbour)
                             
        # for each city not in visited, do a bfs 
        provincies = 0
        visited = set()
        
        for city in graph.keys():
            if city not in visited:
                bfs(graph, city)
                provincies += 1
                
        return provincies
                    
       

s = Solution()
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))