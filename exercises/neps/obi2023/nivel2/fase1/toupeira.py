"""
grafo bidirecionado
para cada caminho descrito
detectar se é possível
s = nodes
t = edges

criar uma lista de adjascência do grafo
para cada item da lista de circuitos
    fazer uma modificação de um dfs sabendo se existe o circuito
"""

def main():
    def possivel(edges, caminho):
        for i in range(2, len(caminho)):
            if caminho[i - 1] not in edges.keys():
                return 0 
            if caminho[i] not in edges.keys():
                return 0 
            if caminho[i] not in edges[caminho[i-1]]:
                return 0
        
        return 1
    
    
    s, t = [int(x) for x in input().split()]
    
    # lista de adjascência
    edges = {x: set() for x in range(1, s + 1)}
    
    # lista de passeios
    passeios = []
    
    # n de caminhos possíveis
    possiveis = 0
    
    for _ in range(t):
        x, y = [int(x) for x in input().split()]
        edges[x].update({x, y})
        edges[y].update({x, y})
        
    p = int(input())
    for _ in range(p):
        passeios.append([int(x) for x in input().split()])
     
        
    for passeio in passeios:
        possiveis += possivel(edges, passeio)
    
    print(possiveis)
        
        

if __name__ == "__main__":
    main()