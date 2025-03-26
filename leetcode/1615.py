"""
fazer a conta da network rank para cada par:
    criar um dicionário com um set dos nodes que se conectam a essa chave, para cada par, adicionar o valor do set dos dois e um só
adicionar esse valor a uma lista
ao final do processo, retornar o maior valor da lista (que será a maior network rank de algum par)
"""

from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        edges = defaultdict(set)
        
        for f, t in roads:
            # tem uma ponte entre os dois
            edges[f].add(t)
            edges[t].add(f)
            
        # print(edges)
        
        maximal = 0
        for i in range(n):
            for j in range(i + 1, n):
                network = len(edges[i]) + len(edges[j])
                # print(f'{i}, {j} -> {network}')
                if j in edges[i]:
                    network -= 1
                    
                maximal = max(maximal, network)
         
        return maximal
                
                
s = Solution()
n = 71
roads = [[52,8],[51,55],[12,30],[61,63],[34,9],[49,48],[21,67],[5,24],[46,25],[0,34],[36,0],[16,21],[42,2],[37,64],[35,29],[46,14],[0,5],[43,9],[1,64],[4,7],[0,27],[44,69],[5,51],[33,13],[41,58],[31,67],[48,27],[48,14],[34,62],[8,30],[25,54],[19,53],[57,9],[48,2],[2,5],[0,17],[47,30],[67,35],[17,14],[49,1]]

print(s.maximalNetworkRank(n, roads))