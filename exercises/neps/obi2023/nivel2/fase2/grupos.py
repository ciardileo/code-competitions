"""
contar quantas restrições de pares que querem ficar juntos ou separados são quebradas com o grupo montado
para integrante do grupo, checar quantos integrantes que ele não quer ficar estão no grupo e checar quantos integrantes que ele quer ficar não estão no grupo
cada restrição violada nós devemos tirar da lista para não ser contada duas vezes
https://neps.academy/br/exercise/2436
"""


def main():
	E, M, D = [int(x) for x in input().split()]
	same_groups = []
	different_groups = []
	groups = []
	result = 0

	for i in range(M):
		X, Y = [int(x) for x in input().split()]
		same_groups.append((X, Y))

	for i in range(D):
		X, Y = [int(x) for x in input().split()]
		different_groups.append((X, Y))

	for i in range(int(E / 3)):
		groups.append([int(x) for x in input().split()])

	students_groups = {}
	for group in groups:
		for student in group:
			students_groups[student] = group

	for X, Y in same_groups:
		if Y not in students_groups[X]:
			result += 1

	for X, Y in different_groups:
		if Y in students_groups[X]:
			result += 1

	print(result)


if __name__ == "__main__":
	main()
