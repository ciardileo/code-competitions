"""
cada aluno pertence a um time
amigos tem que estar no mesmo time
determinar o número máximo de times = número de grafos desconexos no grafo geral
https://neps.academy/br/exercise/309
"""

from collections import deque, defaultdict

def main():
    
    def bfs(graph, start, visited):
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            
            for friend in graph[node] - visited:
                queue.append(friend)
                visited.add(friend)
                
        return visited
    
    # recebe o número de alunos e o número de conexões
    N, M = [int(x) for x in input().split()]
    
    # cria uma lista de adjacência
    graph = defaultdict(set)
    
    # preenche o grafo com as ligações
    for _ in range(M):
        i, j = [int(x) for x in input().split()]
        
        graph[i].add(j)
        graph[j].add(i)
    
    visited = set()    
    teams = 0
    
    for aluno in range(1, N + 1):
        if aluno not in visited:
            visited.update(bfs(graph, aluno, visited))
            teams += 1 
            
    print(teams)
    
    
if __name__ == "__main__":
    main()