"""
espaço M x N (numerado de 1 a N - 0 a N - 1 no código)
K câmeras
As câmeras instaladas observam alguma direção até o final do espaço
A entrada está no 0, 0 e a saída em N, M
Determinar se é possível entrar e sair sem ser visto pelas câmeras

Caso L:
	para cada espaço da posição da câmera até o final do mapa, preencher com 1
Caso O:
	para cada espaço do começo da coluna até a posição da câmera, preencher com 1
Caso N:
	para cada espaço do começo da linha até a posição da câmera, preencher com 1
Caso S:
	para cada espaço da posição da câmera até o final da linha, preencher com 1

[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
"""


def main():

	# monta o mapa posicionando as câmeras
	def camera(y, x, d):
		match d:
			case "L":
				for i in range(x, N):
					cam_map[y][i] = 1

			case "O":
				for i in range(x + 1):
					cam_map[y][i] = 1

			case "N":
				for i in range(y + 1):
					cam_map[i][x] = 1

			case "S":
				for i in range(y, M):
					cam_map[i][x] = 1

	def dfs(row, col):
		if row == M - 1 and col == N - 1:
			return "S"

		for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			new_row, new_col = x + row, y + col
			if 0 <= new_row < M and 0 <= new_col < N:
				if cam_map[new_row][new_col] == 0:
					cam_map[new_row][new_col] = 1
					if dfs(new_row, new_col) == "S":
						return "S"

		return "N"

	# colunas, linhas e cameras
	N, M, K = [int(x) for x in input().split()]

	# 1 - espaço vigiado, 0 - espaço livre
	cam_map = [[0] * N for _ in range(M)]

	for _ in range(K):
		col, row, direction = input().split()
		camera(int(row) - 1, int(col) - 1, direction)

	print(dfs(0, 0, ))


if __name__ == "__main__":
	main()
