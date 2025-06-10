"""
referências diretas - nodes conectados
referências sequenciais - nodes que se encontram em algum momento
referenciais sequenciais são bidimensionais, diretas nao
"""

from collections import defaultdict, deque

def main():
    def bfs(graph, start, end):
        visited = set(start)
        queue = deque([(0, start)])
        
        while queue:
            current_level, current_page = queue.popleft()
            
            if current_page == end:
                return current_level
            
            for reference in graph[current_page] - visited:
                visited.add(reference)
                queue.append((current_level + 1, reference))
                
        return visited
    
    n_referencias = int(input())
    graph = defaultdict(set)
    pags = []
    
    for _ in range(n_referencias):
        pag1, pag2 = input().split()
        
        if pag1 not in pags:
            pags.append(pag1)
            
        if pag2 not in pags:
            pags.append(pag2)
            
        graph[pag1].add(pag2)
        
    input()
    
    pag_inicial, pag_final = input().split()
    
    pags.sort()
    for i in range(len(pags)):
        if i > 0:
            graph[pags[i]].add(pags[i-1])
            graph[pags[i-1]].add(pags[i])
        if i < len(pags) - 1:
            graph[pags[i]].add(pags[i+1])
            graph[pags[i+1]].add(pags[i])
    
    # print(pags)
    # print(*graph.items(), sep="\n")
    
    print(bfs(graph, pag_inicial, pag_final))
    
    
if __name__ == "__main__":
    main()