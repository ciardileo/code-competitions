"""
pomar = matriz de n linhas e m colunas
cada celula representa o numero de frutas
"""

n, m = [int(x) for x in input().split()]

orchard = []
for _ in range(n):
    orchard.append([int(x) for x in input().split()])
    
def max_fruits_collected(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # Initialize the dp matrix with the same dimensions as the matrix
    dp = [[-float('inf')] * m for _ in range(n)]
    
    # Traverse the matrix to fill the dp array
    for i in range(n):
        for j in range(m):
            if i > 0:
                for k in range(i):
                    dp[i][j] = max(dp[i][j], matrix[i][j] - matrix[k][j])
            if j > 0:
                for l in range(j):
                    dp[i][j] = max(dp[i][j], matrix[i][j] - matrix[i][l])
    
    # Find the maximum value in the dp array
    max_fruits = -float('inf')
    for i in range(n):
        for j in range(m):
            if i > 0 or j > 0:  # Ensure at least one move
                max_fruits = max(max_fruits, dp[i][j])
    
    return max_fruits + 1 if max_fruits != -float('inf') else 0

    
    return max_fruits + 1 

print(max_fruits_collected(orchard))