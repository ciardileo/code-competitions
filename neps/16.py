"""
contar quantas vezes cada inteiro vai aparecer na barra
"""

def main():
    N, M = [int(x) for x in input().split()]  # tamanho da barra do cofre, quantidade de mexidas
    barra = [int(x) for x in input().split()]
    posicoes = [int(x) for x in input().split()]
    
    # matriz de prefix sum: prefix[num][pos] = qtd de vezes que ele aparece
    prefix = [[0] * N for _ in range(10)]
    
    for num in range(N):
        pos_atual = barra[num]
        for i in range(num, N):
            prefix[pos_atual][i] += 1
            
    print(*prefix, sep='\n')
    
    # somando os numeros
    result = [0 for _ in range(10)]
    for i in range(M):
        for j in range(10):
            result[j] += prefix[j][posicoes[i-1]]
            
    print(*result, sep=" ")
        
    
if __name__ == "__main__":
    main()