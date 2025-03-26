""" 
matrix N x M
parede é . e prateleira é #
o vazamento é o O
só existem prateleiras nas linhas pares 
Se c(i, j) == . , ele deve virar o se:
- c(i-1, j) = 0
- c(i, j -1) = 0 e c(i+1, j -1) = #
- c(i, j +1) = 0 e c(i+1, j -1) = #
vem de cima, ou dos lados caso haja uma prateleira na diagonal inferior no lado
-------------------
começando no vazamento, independente de tudo, a chuva vai espalhar para a esquerda e direita se não tiver prateleira e se a agua estiver em cima de uma prateleira
a chuva espalhará para baixo se não houver prateleiras

 se eu estiver em cima de uma prateleira: espalhar(esquerda, direita)
 se não: espalhar para baixo
 
https://neps.academy/br/exercise/469
"""

from collections import deque

def main():
    # linhas, colunas
    N, M = [int(x) for x in input().split()]
    
    # matrix do mapa
    matrix = []
    
    # preenchendo a matriz
    for _ in range(N):
        matrix.append([x for x in input()])
    
    start = (0, matrix[0].index('o'))
    
    def bfs(matrix, start):
        queue = deque([start])
        
        while queue:
            row, col = queue.popleft()
            
            if row < N - 1:
                if col != 0 and col < M - 1:
                    if matrix[row+1][col] == '#':
                        if matrix[row][col + 1] == '.':
                            matrix[row][col +1] = 'o'
                            queue.append((row, col + 1))
                        
                        if matrix[row][col -1] == '.':
                            matrix[row][col -1] = 'o'
                            queue.append((row, col - 1))
                
                if matrix[row + 1][col] == '.':
                    matrix[row+1][col] = 'o'
                    queue.append((row+1, col))
                    
        
        return matrix
    
    matrix = bfs(matrix, start)
    for l in matrix:
        print(*l, sep='')
    
        
    
if __name__ == "__main__":
    main()


