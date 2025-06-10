"""
achar quantos intervalos da sequência são iguais a K
"""

def main():
    N, K = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    
    p = [0] * (N + 1)
    for i in range(N):
        p[i+1] = p[i] + nums[i]
    
    cumulative_sum = 0
    count = 0
    # Inicializamos o dicionário com {0: 1} para lidar com somas que começam desde o início
    prefix_sum_counts = {0: 1}
    
    for num in nums:
        cumulative_sum += num  # Atualizamos a soma acumulada
        
        # Verificamos se (cumulative_sum - S) está no dicionário
        if cumulative_sum - K in prefix_sum_counts:
            count += prefix_sum_counts[cumulative_sum - K]  # Adicionamos o número de tais subsequências ao count
        
        # Atualizamos o dicionário com a soma acumulada atual
        if cumulative_sum in prefix_sum_counts:
            prefix_sum_counts[cumulative_sum] += 1
        else:
            prefix_sum_counts[cumulative_sum] = 1
        
    print(count)  # Imprimimos o número total de subsequências cuja soma é igual a S
if __name__ == "__main__":
    main()