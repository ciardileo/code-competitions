"""
introdução a árvores
"""

from collections import defaultdict

def main():
    def dfs(node):
        count = 0
        
        for subordinado in grafo[node]:
            count += dfs(subordinado) + 1
            
        subordinados[node - 1] = count
        return count
    
    funcionarios = int(input())  # N
    
    grafo = defaultdict(set)
    subordinados = [0] * funcionarios
    
    chefes = [int(x) for x in input().split()]
    
    for i in range (2, len(chefes) + 2):
        grafo[chefes[i - 2]].add(i)
    
    dfs(1)
            
    print(subordinados)

    
    
if __name__ == "__main__":
    main()