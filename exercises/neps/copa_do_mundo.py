"""
16 times disputam 15 jogos na fase final
lição: desenhar e escrever em portugues antes de resolver o problema
lição: não se preocupar com repetir código, primeiro focar em resolver o problema
"""


# passa os vencedores de fase
def passagem_de_fase():
	global fase_atual

	# adicionando os times que passaram em outra lista
	for i in range(len(resultados)):
		if resultados[i] == 1:
			proxima_fase.append(fase_atual[i][1])
		else:
			proxima_fase.append(fase_atual[i][0])

	# passa os times para a fase_atual
	fase_atual.clear()
	fase_atual = [[proxima_fase[x], proxima_fase[x + 1]] for x in range(0, len(proxima_fase), 2)]
	proxima_fase.clear()

	# limpa os resultados
	resultados.clear()


# recebe os valores dos jogos e computa o vencedor
def fase(n):
	for i in range(n):
		time1, time2 = [int(x) for x in input().split()]

		if time1 > time2:
			resultados.append(0)
		else:
			resultados.append(1)


# listas dos times
fase_atual = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
proxima_fase = []
resultados = []

# ordena os jogos iniciais
fase_atual = [[fase_atual[x], fase_atual[x + 1]] for x in range(0, len(fase_atual), 2)]

# oitavas
fase(8)
passagem_de_fase()

# quartas
fase(4)
passagem_de_fase()

# semis
fase(2)
passagem_de_fase()

# final
fase(1)
print(fase_atual[0][resultados[0]])
