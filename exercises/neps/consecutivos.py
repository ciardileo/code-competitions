"""
n inteiros
pontos = tamanho da maior sequencia
"""


def contagem_pontos():
	sequencia = 1
	maior_sequencia = 0

	for i in range(1, len(numeros)):
		if numeros[i] == numeros[i - 1]:
			sequencia += 1
			if sequencia > maior_sequencia:
				maior_sequencia = sequencia
		else:
			if sequencia > maior_sequencia:
				maior_sequencia = sequencia

			sequencia = 1

	return maior_sequencia


n = int(input())
numeros = [int(x) for x in input().split()]

print(contagem_pontos())
