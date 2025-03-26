"""
1971. Easy - Find if Path Exists in Graph
Bi-directional with N vertices 
edges = [[0, 1], [2, 1], [0, 2]]
"""

from collections import deque


class Solution:
    def list_to_dict(self, edges, n):
        graph = {v: set() for v in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            
        return graph
    
    def bfs(self, graph, start, destination):
        visited, queue = set([start]), deque([start])
        
        while queue:
            v = queue.popleft()
            
            if v == destination:
                return True
            
            visited.add(v)
            
            for connected in graph[v] - visited:
                queue.append(connected)
        
        return False
    
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = self.list_to_dict(edges, n)
        return self.bfs(graph, source, destination)
        
        
        
        
s = Solution()
print(s.validPath(6, [[0, 1], [1, 2], [2, 0]], 0, 2))