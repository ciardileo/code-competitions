"""
uma matrix do mapa é nos dada, onde + é parede e . é espaço vazio.
devemos retornar o menor número de movimentos até uma saída, se ela existir
toda saída é um espaço vazio nas bordas, que não sejam a entrada
não é permitido andar na diagonal
"""

"""
solution:
1. criar uma função que verifica se aquela posição é uma saída:
    para ser uma saída, pelo menos uma das coordenadas tem que ser 0 ou len(matrix)
2. criar uma função de bfs que verifica primeiramente se existe saída
    criar função que verifica se o movimento é válido
3. fazer uma modificação na função de bfs para contar os números de passos até o alvo
"""

from collections import deque


class Solution:
    def is_exit(self, matrix, coordenates):
        
        row, col = coordenates
        
        if row == 0 or row == len(matrix) - 1:
            return True
        
        if col == 0 or col == len(matrix[0]) - 1:
            return True
        
        return False
    
    def is_valid_move(self, matrix, coordenates):
        row, col = coordenates
        if row < 0 or row >= len(matrix):
            return False
        
        if col < 0 or col >= len(matrix[0]):
            return False
        
        if matrix[row][col] == "+":
            return False
        
        return True
    
    
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True
        queue = deque()
        queue.append([entrance, 0])
        
        while queue:
            coordenates, steps = queue.popleft()
            row, col = coordenates
            
            if self.is_exit(maze, (row, col)) and [row, col] != entrance:
                return steps
            
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if self.is_valid_move(maze, (row + i, col + j)) and visited[row + i][col + j] == False:
                    visited[row][col] = True
                    queue.append([[row + i, col + j], steps + 1])
                    
        return -1

    
s = Solution()
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
print(s.nearestExit(maze, entrance))

"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
         > With BFS, The first exit it comes across is the closest exit
         > Level represents number of steps ahead
        m, n = len(maze), len(maze[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        queue = deque([(*entrance, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True
        
        while queue:
            i, j, level = queue.popleft()
            
            # Return as soon as the nearest exit is found
            # If the current position is on the edges of the grid, thats our exit.
            if (i in {0, m - 1} or j in {0, n - 1}) and [i, j] != entrance:
                # Level represents the shortest distance from the entrance
                return level     
            
            # Iterate through all the directions
            for x, y in directions:
                x, y = x + i, y + j
                # Make sure each neighbour cell is within the boundary and 
                # not yet visited and it is an empty cell
                if 0 <= x < m and 0 <= y < n and \
                not visited[x][y] and maze[x][y] == '.':
                    queue.append((x, y, level + 1))
                    visited[x][y] = True

        return -1

"""