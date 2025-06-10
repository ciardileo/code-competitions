from collections import deque

def is_valid_move(matrix, visited, row, col):
    """
    Verifica se um movimento é válido dentro da matriz, ou seja, se não ultrapassa os limites da matriz,
    se o elemento é zero (permitido) e se o local ainda não foi visitado.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0 and not visited[row][col]

def can_reach_target(matrix, start, target):
    """
    Verifica se é possível alcançar o destino a partir do vértice inicial na matriz.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]  # Inicializa a matriz de visitados como falso

    queue = deque([(start[0], start[1])])  # Inicializa a fila de BFS com o vértice inicial
    visited[start[0]][start[1]] = True  # Marca o vértice inicial como visitado

    while queue:
        row, col = queue.popleft()  # Remove o vértice da fila para processamento

        if (row, col) == target:  # Verifica se o vértice atual é o destino
            return True

        # Verifica os vizinhos do vértice atual
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(matrix, visited, new_row, new_col):  # Verifica se o movimento é válido
                visited[new_row][new_col] = True  # Marca o novo vértice como visitado
                queue.append((new_row, new_col))  # Adiciona o novo vértice à fila de processamento

    return False  # Se chegou até aqui, não encontrou o destino

def read_coordinates():
    """
    Solicita e lê as coordenadas do usuário para um vértice.
    """
    row = int(input("Digite a linha: "))  # Lê a linha do usuário
    col = int(input("Digite a coluna: "))  # Lê a coluna do usuário
    return row, col  # Retorna as coordenadas lidas

def print_matrix(matrix):
    """
    Imprime a matriz.
    """
    for row in matrix:
        print(" ".join(map(str, row)))  # Imprime cada linha da matriz

# Matriz de exemplo
matrix = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0]
]

# Imprime a matriz de exemplo
print("Matriz:")
print_matrix(matrix)

# Solicita e lê as coordenadas do usuário para o vértice inicial
print("\nDigite as coordenadas para o vértice inicial:")
start = read_coordinates()

# Solicita e lê as coordenadas do usuário para o vértice destino
print("Digite as coordenadas para o vértice destino:")
target = read_coordinates()

# Verifica se é possível alcançar o destino a partir do vértice inicial
if can_reach_target(matrix, start, target):
    print("É possível alcançar o destino.")
else:
    print("Não é possível alcançar o destino.")