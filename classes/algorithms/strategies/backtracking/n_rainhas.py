"""
problema das n-rainhas
devemos posicionar as rainhas em um tabuleiro de xadrez N x N de modo que elas não possam se atacar

solução:
    para cada coluna, tentar posicionar uma rainha em uma linha diferente
        a cada posicionamento, checar se há uma rainha na mesma linha, coluna ou diagonais
        se nao, repetir o processo com a próxima coluna
        
    caso ultrapassarmos o número da coluna final, chegamos em um resultado solido
    
solução mais eficiente (guarda as informações se uma linha ou diagonal já teve uma rainha colocada)
def main():
    N = 12
    rows = [0] * N
    diagonals1 = [0] * (2 * N - 1)  # Diagonais principais
    diagonals2 = [0] * (2 * N - 1)  # Diagonais secundárias
    
    def is_valid_move(row, col):
        # Verifica se a linha, a diagonal principal ou a diagonal secundária já têm uma rainha
        if rows[row] or diagonals1[row - col + N - 1] or diagonals2[row + col]:
            return False
        return True
    
    def place_queen(row, col, place):
        rows[row] = place
        diagonals1[row - col + N - 1] = place
        diagonals2[row + col] = place
    
    def n_queens(col=0):
        if col >= N:
            return 1
        
        count = 0
        for row in range(N):
            if is_valid_move(row, col):
                place_queen(row, col, 1)
                count += n_queens(col + 1)
                place_queen(row, col, 0)
        
        return count
    
    print(n_queens())

if __name__ == "__main__":
    main()

"""

def main():
    N = 12
    board = [[0] * N for _ in range(N)]
    
    
    def is_valid_move(row, col):
        # checa a linha
        if 1 in board[row]:
            return False
        
        # Verifica a diagonal superior esquerda
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
    
        # Verifica a diagonal inferior esquerda
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
            
        return True
    
    
    def n_queens(col=0):
        if col >= N:
            return 1
        
        count = 0
        
        for i in range(N):
            if is_valid_move(i, col):
                board[i][col] = 1
                count += n_queens(col + 1)
                board[i][col] = 0
                
        return count
    
    
    print(n_queens())
        
    

if __name__ == "__main__":
    main()