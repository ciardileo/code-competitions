"""
Fazer uma bfs em cada estado iniciando em (0, 0)
Checar todas as vizinhas de cada casa e fazer as condições
Atualizar uma nova matriz e passá-la como parâmetro para o próximo passo
"""

from collections import deque

def atualiza_estado(estado_atual, N):
    visitados = set()  # controle para não visitar a mesma célula mais de uma vez
    novo_estado = [[0] * N for _ in range(N)]
    fila = deque([(0, 0)])
    positions = ((1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1))
    
    while fila:
        vizinhas_vivas = 0
        row, col = fila.popleft()
        
        # checa todos os vizinhos
        for x, y in positions:
            new_row = row + x
            new_col = col + y
            
            if 0 <= new_col < N and 0 <= new_row < N:
                
                if estado_atual[new_row][new_col] == 1:
                    vizinhas_vivas += 1
                    
                if (new_row, new_col) not in visitados:
                    fila.append((new_row, new_col))
                    visitados.add((new_row, new_col))
                    
        if estado_atual[row][col] == 1:
            if vizinhas_vivas == 2 or vizinhas_vivas == 3:
                novo_estado[row][col] = 1
            else:
                novo_estado[row][col] = 0
        else:
            if vizinhas_vivas == 3:
                novo_estado[row][col] = 1
            else:
                novo_estado[row][col] = 0
                    
    return novo_estado

def main():
    # variáveis
    matriz = []
    
    # inputs
    N, Q = [int(x) for x in input().split()]  # dimensões da matriz, número de passos
    
    for _ in range(N):
        matriz.append([int(x) for x in input()])

    # repetição das fases
    for _ in range(Q):
        matriz = atualiza_estado(matriz, N)
    
    for linha in matriz:
        print(*linha, sep="")
        
    
    
    
if __name__ == "__main__":
    main()