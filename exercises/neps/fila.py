"""
fila contem N pessoas
LIÇÃO: EVITAR USAR O INDEX
"""

# adicionando os identificadores da fila inicial
pessoas_fila = int(input())
fila_inicial = [int(x) for x in input().split()]

# criando uma lista das pessoas que saíram
sairam_fila = int(input())
id_saidas = [int(x) for x in input().split()]

# tirando as pessoas que saíram
for pessoa in range(len(id_saidas)):
	fila_inicial.remove(id_saidas[pessoa])

print(*fila_inicial, sep=" ")

