"""
achar a toca do saci, só pode andar na horizontal e vertical
"""

from collections import deque


def main():
	def bfs(x, y):
		queue = deque([(x, y)])
		positions = (
			(1, 0),
			(0, 1),
			(-1, 0),
			(0, -1)
		)

		count = 0

		while queue:
			row, col = queue.popleft()

			for ver, hor in positions:
				new_row = row + ver
				new_col = col + hor

				if 0 <= new_row < N and 0 <= new_col < M:
					if mapa[new_row][new_col] != '0':
						queue.append((new_row, new_col))
						count += 1
						if mapa[new_row][new_col] == '2':
							return count

						mapa[new_row][new_col] = '0'

		return count

	N, M = [int(x) for x in input().split()]

	mapa = []

	for _ in range(N):
		mapa.append(input().split())

	# achar a entrada ou saída
	achou = False
	for i in range(N):
		if '3' in mapa[i]:
			for j in range(M):
				if mapa[i][j] == '3':
					achou = True
					print(bfs(i, j))
					break
		if achou:
			break


if __name__ == "__main__":
	main()