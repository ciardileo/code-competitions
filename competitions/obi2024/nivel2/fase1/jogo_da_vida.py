"""
Matriz N x N
0 ou 1

Se uma célula morta tiver 3 vizinhos vivos, ela vira uma célula viva
Se uma célula morta possuir qualquer qtd de vizinhos vivos diferente 3, continua morta
Se uma célula viva ter 2 ou 3 vizinhos vivos, continua viva
Se uma célula viva tiver mais que 3 ou menos que 2 vizinhos vivos, ela morre.
"""

MOVES = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))

def simular_rodada(matriz, N):
    nova_matriz = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            vizinhos_vivos = 0
            # vizinhos_mortos = 0
            estado = matriz[i][j]
            
            # contagem de vizinhos
            for (delta_y, delta_x) in MOVES:
                nova_linha = (i + delta_y)
                nova_coluna = (j + delta_x)
                # print(nova_linha, nova_coluna)
                # verifica se essa posição está dentro dos limites
                if 0 <= nova_linha < N and 0 <= nova_coluna < N:
                    if matriz[nova_linha][nova_coluna] == 1:
                        vizinhos_vivos += 1
                    # else:
                    #     vizinhos_mortos += 1
            
            # checagem dos parâmetros
            if (estado == 1):
                if vizinhos_vivos == 2 or vizinhos_vivos == 3:
                    nova_matriz[i][j] = 1
                else:
                    nova_matriz[i][j] = 0
                
            else:
                if vizinhos_vivos == 3:
                    nova_matriz[i][j] = 1
                    
            # print(f"Célula {i}, {j}: {vizinhos_mortos} mortos e {vizinhos_vivos} vivos")
    
    return nova_matriz



def main():
    N, Q = list(map(int, input().split()))  # dimensão, número de passos
    matriz = []
    
    for _ in range(N):
        matriz.append(list(map(int, input())))
        
    # print(matriz)
        
    # início da simulação
    for _ in range(Q):
        matriz = simular_rodada(matriz=matriz, N=N)
        
    # apresentação
    for i in matriz:
        print(*i, sep="")
        

if __name__ == "__main__":
    main()