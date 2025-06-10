"""
cada time tem 1 ou mais alunos
cada aluno só pode ter 1 time
amigos tem que estar no mesmo time
se enumeraram de 1 ate N
há uma lista de pares de números que representam amigos
lição: APRENDER SOBRE GRAFOS
"""

# recebe a entrada inicial
num_alunos, tam_lista = [int(x) for x in input().split()]

# listas padrões
alunos = set([i for i in range(num_alunos)])
pares_amigos = list()
alunos_chamados = set()
grupos = {}

# pega a lista de pares amigos
for i in range(tam_lista):
	pares_amigos.append([int(x) for x in input().split()])

# cria os grupos:
for par in pares_amigos:
	# cria um novo grupo caso os dois não sejam repetidos
	if par[0] not in alunos_chamados and par[1] not in alunos_chamados:
		alunos_chamados.update([par[0], par[1]])
		grupos[par[0]] = {par[0], par[1]}
	elif par[0] in alunos_chamados and par[1] not in alunos_chamados:
		alunos_chamados.add(par[1])
		chave_grupo = [chave for chave, valor in grupos.items() if par[0] in valor]
		grupos[chave_grupo[0]].add(par[1])
	elif par[0] not in alunos_chamados and par[1] in alunos_chamados:
		alunos_chamados.add(par[0])
		chave_grupo = [chave for chave, valor in grupos.items() if par[1] in valor]
		grupos[chave_grupo[1]].add(par[0])
	else:
		chave_grupo1 = [chave for chave, valor in grupos.items() if par[0] in valor]
		chave_grupo2 = [chave for chave, valor in grupos.items() if par[1] in valor]
		if chave_grupo1 != chave_grupo2:
			grupos[chave_grupo1[0]].update(grupos[chave_grupo2[0]])
			del grupos[chave_grupo2[0]]

if len(alunos - alunos_chamados) > 1:
	print(len(grupos) + 1)
else:
	print(len(grupos))
