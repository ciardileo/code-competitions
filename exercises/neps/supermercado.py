"""
dinheiro = B (bit)
preços são anunciados como X bits por Y gramas
determinar menor valor que maria pode gastas para comprar 1 quilo
"""

n_supermercados = int(input())
precos = []

for i in range(n_supermercados):
	bits, gramas = [float(x) for x in input().split()]
	preco_quilo = 1000 / gramas * bits
	precos.append(preco_quilo)

precos.sort()
print(f"{precos[0]:.2f}")
