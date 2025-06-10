"""
Algumas pessoas conseguem fazer cálculos matemáticos com uma velocidade impressionante. Laurinha tem essa habilidade! Um cálculo que ela consegue fazer muito rapidamente é, dados três números inteiros S, A, e B, determinar quantos números do intervalo [A, B] têm a soma de seus dígitos igual a S.

Por exemplo, se S = 3, A = 10 e B = 30, então a reposta é 3, pois existem três números no intervalo [10,30] cuja soma dos dígitos é igual a três: 12, 21 e 30.

Sua tarefa é escrever um programa de computador para, dados os três números, tentar calcular a resposta mais rapidamente do que Laurinha consegue.

Entrada
A primeira linha da entrada contém um número inteiro S, o valor da soma dos dígitos. A segunda e a terceira linhas contêm respectivamente os inteiros A e B.

Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, quantos números no intervalo dado têm a soma de dígitos indicada.
"""

s = int(input())  # soma
a = int(input())  # início do intervalo
b = int(input())  # fim do intervalo

soma = int()
numeros = int()

for i in range(a, b+1):
	soma = 0
	for j in str(i):
		soma += int(j)

	if soma == s:
		numeros += 1

print(numeros)
