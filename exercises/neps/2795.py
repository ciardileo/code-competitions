def main():
    # Função para calcular o número concatenado de dois dígitos
    def concatena(a, b):
        return int(str(a) + str(b))
    
    # Lê os valores de N e Q
    N, Q = map(int, input().split())
    
    # Lê a lista de números
    numeros = list(map(int, input().split()))
    
    # Inicializa a matriz prefix_sum para armazenar as somas das concatenações
    prefix_sum = [[0] * N for _ in range(N)]
    
    # Pré-processa todas as concatenações possíveis e preenche prefix_sum
    for i in range(N):
        for j in range(i + 1, N):
            # Soma a concatenação de todos os pares (i, j) e (j, i)
            concat_value = concatena(numeros[i], numeros[j]) + concatena(numeros[j], numeros[i])
            prefix_sum[i][j] = concat_value

    # Acumula as somas para todos os subintervalos
    for i in range(N):
        for j in range(i + 1, N):
            # Acumula a soma dos pares até o intervalo [i, j]
            prefix_sum[i][j] += prefix_sum[i][j - 1] if j - 1 >= i else 0
    
    resultado = []
    
    # Processa cada query
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1  # Ajusta para índice zero
        R -= 1  # Ajusta para índice zero
        
        # Se o intervalo tem tamanho 1, o potencial é zero (não há pares)
        if R == L:
            resultado.append(0)
        else:
            resultado.append(prefix_sum[L][R])
    
    # Imprime todos os resultados de uma vez
    print(*resultado, sep="\n")

if __name__ == "__main__":
    main()
