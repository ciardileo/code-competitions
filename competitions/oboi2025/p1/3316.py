def main():
    N, M = map(int, input().split())  # número de lançamentos, número para ser pomposo
    sequencia = list(map(int, input().split()))
    prefix_sum = [0 for _ in range(N + 1)]
    maior_sequencia = 0
    
    # preenchendo o array de prefix sum
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + sequencia[i - 1]
        # if prefix_sum[i] % M == 0:
        #     maior_sequencia = i
        
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            if (prefix_sum[j] - prefix_sum[i]) % M == 0:
                if (j - i) > maior_sequencia:
                    maior_sequencia = j - i
            
    # print(prefix_sum) 
    print(maior_sequencia)
    
    
if __name__ == "__main__":
    main()