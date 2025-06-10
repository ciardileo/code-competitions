"""
A média de três números inteiros A, B e C é (A + B + C)/3. A mediana de três números inteiros é o número que ficaria no meio se os três números fossem ordenados em ordem não-decrescente.

Sua tarefa é escrever um programa que, dados dois números inteiros distintos A e B, calcule o menor inteiro possível C tal que a média e a mediana de A, B e C sejam iguais.

Entrada
A entrada é composta de uma única linha contendo dois números inteiros A e B.

Saída
Seu programa deve produzir uma única linha, contendo um único número, o menor inteiro possível C tal que a média e a mediana de A, B e C são iguais.
"""

# não consegui resolver, resolução do site : https://noic.com.br/materiais-informatica/comentario/obi-2021/fase2-turnoa-p2/

a, b = list(map(int, input().split()))

if a > b:
	a, b = b, a  # 'a' vira o menor elemento

# Vamos fazer o elemento 'a' ser a mediana.
c = a - (b - a)  # c < a < b

print(c)

# def descobrir_mediana(numeros):
# 	if len(numeros) % 2 == 0:
# 		_mediana = (numeros[int(len(numeros)) / 2] + numeros[int(len(numeros)) / 2 - 1]) / 2
# 	else:
# 		_mediana = lista[len(lista) // 2]
# 	return _mediana
# lista = list()
# lista.extend([int(a), int(b)])
# cont_positivo = 0
# cont_negativo = 0
# while True:
# 	lista.append(cont_positivo)
# 	lista.sort()
# 	print(lista)
# 	media = sum(lista) / len(lista)
#
# 	mediana = descobrir_mediana(lista)
#
# 	if mediana == media:
# 		print(cont_positivo)
# 		break
#
# 	del lista[lista.index(cont_positivo)]
# 	cont_positivo += 1
#
# 	lista.append(cont_negativo)
# 	lista.sort()
# 	print(lista)
# 	media = sum(lista) / len(lista)
#
# 	mediana = descobrir_mediana(lista)
#
# 	if mediana == media:
# 		print(cont_negativo)
# 		break
#
# 	del lista[lista.index(cont_negativo)]
# 	cont_negativo -= 1
