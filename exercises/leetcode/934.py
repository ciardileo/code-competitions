""" 
grid n x n
1 - island
0 - water

percorrer o grid até achar um lugar com terra
aplicar um dfs nesse lugar com terra para encontrar toda sua extensão
marcar todos os lugares passados com um 2, indicando uma ilha diferente
para cada borda que for mar dessa ilha 1:
aplicar um bfs até achar um 1, que seria outra ilha
comparar os bfs até achar o menor

"""

from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        def dfs(x, y):
            grid[x][y] = 2
            start_points.add((x, y))
            for w, z in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = x + w, y + z
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                        dfs(x, y)
        
        def bfs(start):
            queue = deque((start, 0))
     
            while queue:
                coord, level = queue.popleft()
                grid[coord[0]][coord[1]] == 3
                
                if grid[coord[0]][coord[1]] == 1:
                    return level
                
                for neighbour in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = coord[0] + neighbour[0], coord[1] + neighbour[1]
                    
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 0:
                            queue.append(((x, y), level + 1))
                        elif grid[x][y] == 1:    
                            return level + 1
                        
            return -1
   
        # descobrindo os limites da primeira ilha
        
        start_points = set()
        for row in range(n):
            if 1 in grid[row]:
                for col in range(n):
                    if grid[row][col] == 1:
                        dfs(row, col)
                        break
                break
         
        # aplicando um bfs partindo de cada borda da outra ilha:
        bridge = float('infinity')
        print(start_points)
        for start in start_points:
            result = bfs(start)
            if result != -1:
                bridge = min(bridge, result)
            
        return bridge
                    
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1
        # Find any land cell, and we treat it as a cell of island A.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break
        
        # Recursively check the neighboring land cell of current cell grid[x][y] and add all
        # land cells of island A to bfs_queue.
        def dfs(x, y):
            grid[x][y] = 2
            bfs_queue.append((x, y))
            for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y)
        
        # Add all land cells of island A to bfs_queue.
        bfs_queue = []
        dfs(first_x, first_y)
        
        distance = 0
        while bfs_queue:
            new_bfs = []
            for x, y in bfs_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1

            # Once we finish one round without finding land cells of island B, we will
            # start the next round on all water cells that are 1 cell further away from
            # island A and increment the distance by 1.
            bfs_queue = new_bfs
            distance += 1
"""                   
            
            
    
s = Solution()

grid = [[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]]

print(s.shortestBridge(grid))