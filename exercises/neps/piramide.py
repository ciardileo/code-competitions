"""
criar uma matriz N x N preenchida de 1
até chegar no nível máximo possível:
	fazer um bfs na matrix, passando por todos os pontos e os que forem igual a level e cercados em todas as direções apenas por números iguais a level devem ser mudados para level + 1
Nesse problema não era necessário fazer um bfs, poderia apenas fazer uma fila com todas as posições, e para cada um verificar se ele tem que ser mudado para o próximo nível
"""

from collections import deque


def main():
	# def bfs(piramid, level):
	# 	visited = set()
	# 	to_change = set()
	# 	queue = deque([(0, 0)])
	# 	visited.add((0, 0))
	# 	changed = False
	# 	neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
	#
	# 	while queue:
	# 		x, y = queue.popleft()
	#
	# 		count = 0
	# 		for row, col in neighbours:
	# 			new_row, new_col = x + row, y + col
	# 			if 0 <= new_row < N and 0 <= new_col < N:
	# 				if (new_row, new_col) not in visited:
	# 					queue.append((new_row, new_col))
	# 					visited.add((new_row, new_col))
	#
	# 				if piramid[new_row][new_col] == level:
	# 					count += 1
	#
	# 		if count == 8:
	# 			changed = True
	# 			to_change.add((x, y))
	#
	# 	for x, y in to_change:
	# 		piramid[x][y] = level + 1
	#
	# 	return piramid, changed
	#
	# # dimensão da pirâmide
	# N = int(input())
	#
	# piramid = [[1] * N for _ in range(N)]
	#
	# level = 1
	# while True:
	# 	piramid, changed = bfs(piramid, level)
	# 	if not changed:
	# 		break
	# 	level += 1
	#
	# for row in piramid:
	# 	print(*row, sep=' ')

	# solução mais simples:
	N = int(input())

	"""
	11
	11
	(0, 1)
	1 1 1 
	1 1 1
	1 1 1
	
	distância pra cima: linha
	distância pra esquerda: coluna
	distância pra direita: (N - 1) - coluna
	distância pra baixo: (N - 1) - linha
	"""

	for i in range(N):
		for j in range(N):
			cima = i
			esquerda = j
			direita = N - 1 - j
			baixo = N - 1 - i
			nivel = min(cima, esquerda, direita, baixo) + 1
			print(f"{nivel}", end=' ')
		print()


if __name__ == "__main__":
	main()
