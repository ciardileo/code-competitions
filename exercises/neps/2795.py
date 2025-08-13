"""
o potencial de um intervalo de números (de 1 a 9) é a soma de todas as combinações de concatenações
sobre uma mesma lista de números, ela perguntará o potencial de diferentes intervalos.
montar um array de prefix sum, calculando previamente o potencial de cada intervalo

lógica do prefix sum:
para cada digito, faz a combinação dele com todos os outros dígitos antes dele
"""

def main():
    N, Q = map(int, input().split())  # número de digitos da lista, quantidade de perguntas
    digitos = list(map(int, input().split()))
    prefix_array = [0 for _ in range(len(digitos) + 1)]
    resultados = []
    
    # criando o prefix sum array
    for i in range(1, len(digitos) + 1):
        prefix_array[i] = prefix_array[i - 1]
        # adiciona o valor das concatenações
        prefix_array[i] += (digitos[i - 1] * 10) + (digitos[i - 1])
          
    # lendo as perguntas 
    for _ in range(Q):
        L, R = map(int, input().split())  # intervalo
        resultados.append((prefix_array[R] - prefix_array[L - 1]) * (R - L))

    print(*resultados, sep="\n")

    
if __name__ == "__main__":
    main()