"""
dfs básico percorrendo os H até achar um H que não tem vizinhos não visitados
"""

from collections import deque

def main():
    # def dfs(x, y):
    #     _map[x][y] = "V"
        
    #     for ver, hor in positions:
    #         row = x + ver
    #         col = y + hor
            
            
    #         if 0 <= row < rows and 0 <= col < cols:
    #             if _map[row][col] == "H":
    #                 result = dfs(row, col)
    #                 return result
                
    #     return (x, y)
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        while queue:
            row, col = queue.popleft()
            
            achou = False
            for ver, hor in positions:
                new_row = row + ver
                new_col = col + hor
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if _map[new_row][new_col] == "H":
                        achou = True
                        _map[new_row][new_col] = 'V'
                        queue.append((new_row, new_col))
                        
            if not achou:
                return (row, col)
    
    rows, cols = [int(x) for x in input().split()]
    
    _map = []
    positions = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    )
    
    # filling the map
    for _ in range(rows):
        line = input()
        
        _map.append([x for x in line])
    
    terminou = False
    for i in range(rows):
        if 'o' in _map[i]:
            for j in range(cols):
                if _map[i][j] == 'o':
                    final_position = bfs(i, j)
                    terminou = True
                    break
        elif terminou:
            break
        
    
    print(final_position[0] + 1, final_position[1] + 1)
    
    
if __name__ == "__main__":
    main()