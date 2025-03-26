"""
encontrar algum node que não tenha ligações, mas que todos os outros se ligam com ele
se não encontrar ou encontrar mais de um
"""

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph = {x: [0, 0] for x in range(1, n + 1)} # (ligações, ligados a ele)
        
        for x, y in trust:
            graph[x][0] += 1 
            graph[y][1] += 1 
            
        for node, relation in graph.items():
            if relation[0] == 0 and relation[1] == n - 1:
                return node
        
        return -1        
        
    
s = Solution()
print(s.findJudge(3, [[1,3],[2,3],[3,1]]))