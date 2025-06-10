"""
móbiles são como árvores
cada móbile tem um submóbile
um móbile é balanceado se, para cada peça:
    todos os submóbiles pendurados nela são compostos pelo mesmo número de peças (número de peças ligadas a ele + ele mesmo)
"""

from collections import defaultdict

def main():
    pecas = int(input())    
    arvore = defaultdict(set)
    qtd_conexoes = {i: 1 for i in range(pecas + 1)}
    
    for _ in range(pecas):
        i, j = [int(x) for x in input().split()]
        
        qtd_conexoes[j] += 1
        arvore[j].add(i)
        
    for peca, sub in arvore.items():
        if qtd_conexoes[peca] > 2:
            teste = {qtd_conexoes[x] for x in sub}
            if len(teste) != 1:
                print("mal")
                return
                
    print("bem")
    
    
    
    
    
if __name__ == "__main__":
    main()

