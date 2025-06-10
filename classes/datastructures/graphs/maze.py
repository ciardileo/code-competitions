"""
All the concepts I know about graphs

DFS (Depth-First Search):
 - Utiliza recursão para visitar todos os espaços;
 - Complexidade O(V + E)

"""

from collections import defaultdict, deque

def main():
	def dfs(x, y, path=None):
		if path is None:
			path = []

		# Marca o node atual como visitado
		maze[x][y] = 2

		# Adiciona o lugar atual ao caminho
		path.append((x, y))

		# Se o destino foi alcançado, para a execução e retorna o caminho
		if (x, y) == (total_rows - 1, total_cols - 1):
			print(f"Cheguei: {(x, y)}")
			print(f"Caminho encontrado: {path}")
			return path

		# Chama a função para os vizinhos, desde que não tenham sido visitados e estejam dentro dos limites
		for ver, hor in movements:
			row = x + ver
			col = y + hor

			# Se estiver dentro dos limites
			if 0 <= row < total_rows and 0 <= col < total_cols:

				# E não estiver sido visitado nem bloqueado
				if maze[row][col] == 0:
					result = dfs(row, col, path)
					if result:  # Se a chamada recursiva encontrou o caminho, retorna o resultado
						return result

		# Remove a última posição se a recursão voltou (backtracking)
		path.pop()

		return None  # Retorna None se não encontrar o caminho

	def bfs(x, y):
		...

	def dijkstra(x, y):
		...

	maze = [
		[0, 1, 0, 0, 1, 0],
		[0, 1, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0],
		[0, 0, 1, 0, 1, 0]
	]

	maze_result = [
		[0, 1, 0, 0, 1, 0],
		[0, 1, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0],
		[0, 0, 1, 0, 1, 0]
	]

	total_rows, total_cols = len(maze), len(maze[0])

	movements = (
		(-1, 0),  # cima
		(1, 0),  # baixo
		(0, -1),  # esquerda
		(0, 1),  # direita
	)

	starting_row = int(input("Starting row: "))
	starting_col = int(input("Starting col: "))

	opt = int(input("Option (1 - dfs, 2 - bfs, 3 - djikstra): "))

	print("=" * 25)

	print(*maze, sep='\n')

	print("=" * 25)

	match opt:
		case 1:
			path = dfs(starting_row, starting_col)

			if path:
				for x, y in path:
					maze_result[x][y] = 2

			print(*maze_result, sep='\n')

		case 2:
			bfs(starting_row, starting_col)

		case 3:
			dijkstra(starting_row, starting_col)


if __name__ == "__main__":
	main()
