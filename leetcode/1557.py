"""
retornar a menor lista possível dos vertices de forma que com eles é possivel alcançar todos os nodes
1. organizar uma lista dos nodes apenas com o número de incomings e outcoming edges
2. a resposta será todos os os nodes que não tiverem incoming edges mas tiverem mais de 0 outcoming edges
"""
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        incoming_edges = defaultdict(int)
        
        for f, t in edges:
            incoming_edges[f] += 0
            incoming_edges[t] += 1
            
        result = []
            
        for node in incoming_edges.items():
            print(node)
            if node[1] == 0:
                result.append(node[0])
                
        return result
    
    
""" 
better solution:
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tos = set(edge[1] for edge in edges)
        return [i for i in range(n) if i not in tos]
 
"""