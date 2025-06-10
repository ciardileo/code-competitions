"""
um quadrado mágico é uma matriz n x n inteiros, em que todas as linhas, colunas e diagonais tem a mesma soma
"""


def verifica_quadrado_magico():
	soma_atual = 0
	soma_atual2 = 0
	# soma
	soma = sum(quadrado[0])

	# soma das linhas
	for linha in quadrado:
		if sum(linha) != soma:
			return -1

	# Soma das colunas
	for j in range(n):
		soma_coluna = 0
		for i in range(n):
			soma_coluna += quadrado[i][j]
		if soma_coluna != soma:
			return -1

	soma_atual = 0

	# soma das diagonais
	soma_diag_principal = sum(quadrado[i][i] for i in range(n))
	if soma_diag_principal != soma:
		return -1

	# Soma da diagonal secundária
	soma_diag_secundaria = sum(quadrado[i][n - i - 1] for i in range(n))
	if soma_diag_secundaria != soma:
		return -1

	return soma


n = int(input())
quadrado = []

for i in range(n):
	quadrado.append([int(x) for x in input().split()])

print(verifica_quadrado_magico())
