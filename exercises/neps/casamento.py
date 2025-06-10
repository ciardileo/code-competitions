"""
- adiionar zeros a esquerda pros números terem o mesmo numero de digitos
- compara os digitos da esquerda pra direita, o digito de menor valor é eliminado
- caso não sobrar dígitos, o número é -1
- escrever o par formado em ordem crescente
"""

# entradas
a = input()
b = input()
a2, b2 = str(), str()

if len(a) > len(b):
	b = "0" * (len(a) - len(b)) + b
elif len(b) > len(a):
	a = "0" * (len(b) - len(a)) + a

for alg in range(len(a)):
	if int(a[alg]) > int(b[alg]):
		a2 += a[alg]
	elif int(b[alg]) > int(a[alg]):
		b2 += b[alg]
	else:
		a2 += a[alg]
		b2 += b[alg]

lista = []

if len(a2) == 0:
	a2 += "-1"
elif len(b2) == 0:
	b2 += "-1"

lista.extend([int(a2), int(b2)])
lista.sort()
print(lista[0], lista[1])

