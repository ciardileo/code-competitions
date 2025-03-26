# NÃO RESOLVIDO
# n = int(input())
# pontos = list()
# parte1 = list()
# parte2 = list()
#
#
# valores = list(map(int, input().split()))
# pontos.extend(valores)
#
# soma = 0
# for i in pontos:
#     soma += i
#     if soma > (sum(pontos) / 2):
#         parte2.append(i)
#     else:
#         parte1.append(i)
#
#
# print(parte1, sum(parte1))
# print(parte2, sum(parte2))
#
# soma1 = 0
# soma2 = 0
# lados_formados = 0
# duas_partes = [(x, y) for x in parte1 for y in parte2]
#
# for item1, item2 in duas_partes:
#     soma1 += item1
#     soma2 += item2
#
#     if soma1 == soma2:
#         lados_formados += 2
#         soma1, soma2 = 0, 0
#
# if lados_formados == 4:
#     print("S")
# else:
#     print("N")
#

#!/usr/bin/env python3

from sys import stdin, stdout

N = int(stdin.readline())

trees = [int(i) for i in stdin.readline().split()]

arc_sum = 0
for i in range(N):
    arc_sum = arc_sum - trees[i]

# apontadores
p,q = 0,0

# contador para o número de semi-circulos de mesmo comprimento
a = 0

# existe retângulo se há pelo menos dois pares de pontos diametralmente opostos
while q != N and a < 2:
    if arc_sum > 0:
        # advance p
        arc_sum = arc_sum - 2*trees[p]
        p += 1
    elif arc_sum < 0:
        # advance q
        arc_sum = arc_sum + 2*trees[q]
        q += 1
    else:
        # advance p and q
        arc_sum = arc_sum - 2*trees[p] + 2*trees[q]
        p += 1
        q += 1
        a += 1

if a >= 2:
    stdout.write('S\n')
else:
    stdout.write('N\n')

