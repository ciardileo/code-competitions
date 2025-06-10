"""
achar o número de intervalos em uma sequencia de numeros que tem a soma igual a S
"""


def main():

    # Leitura dos dados de entrada
    N = int(int(input()))
    S = int(int(input()))
    measurements = list(map(int, input().split()))
    
    cumulative_sum = 0
    count = 0
    # Inicializamos o dicionário com {0: 1} para lidar com somas que começam desde o início
    prefix_sum_counts = {0: 1}
    
    for num in measurements:
        cumulative_sum += num  # Atualizamos a soma acumulada
        print(f'Atual: {num}\nAcumulado: {cumulative_sum}')
        
        # Verificamos se (cumulative_sum - S) está no dicionário
        if cumulative_sum - S in prefix_sum_counts:
            print(f'{cumulative_sum} - {S} está no dicionário, aumenta o count em {prefix_sum_counts[cumulative_sum - S]}')
            count += prefix_sum_counts[cumulative_sum - S]  # Adicionamos o número de tais subsequências ao count
        
        # Atualizamos o dicionário com a soma acumulada atual
        if cumulative_sum in prefix_sum_counts:
            print(f'Já existe no dicionário')
            prefix_sum_counts[cumulative_sum] += 1
        else:
            print('Adicionei ao dicionário')
            prefix_sum_counts[cumulative_sum] = 1
        
    print('-'*25)
    print(f'Resultado final: {count}')  # Imprimimos o número total de subsequências cuja soma é igual a S
    
if __name__ == "__main__":
    main()
