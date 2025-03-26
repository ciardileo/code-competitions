"""
matrix n x m
Montar e pintar a matrix
Começar um bfs a partir do node inicial, e depois contar quantas casas foram visitadas
"""

from collections import deque


def main():
	# initial variables
	rows, cols, start_row, start_col, colored = [int(x) for x in input().split()]

	# creating the matrix
	matrix = [[0] * cols for _ in range(rows)]

	# coloring the matrix
	for _ in range(colored):
		colored_row, colored_col = [int(x) for x in input().split()]
		matrix[colored_row - 1][colored_col - 1] = 1

	# bfs function
	def bfs(matrix, start):
		visited_count, queue = 0, deque([start])
		matrix[start[0]][start[1]] = -1
		while queue:
			row, col = queue.popleft()
			visited_count += 1

			positions = ((1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1))

			for x, y in positions:
				new_row = row + x
				new_col = col + y

				if 0 <= new_row < rows and 0 <= new_col < cols:
					if matrix[new_row][new_col] == 0:
						queue.append((new_row, new_col))
						matrix[new_row][new_col] = -1

		return visited_count

	print(bfs(matrix, (start_row - 1, start_col - 1)))


main()
