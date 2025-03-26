# """
# todo funcionário tem um chefe
# o chefe de todo funcionário entrou na empresa antes dele
# um funcionário está insatisfeito se um dos seus subordinados ganharem mais que ele

# criar um grafo da hierarquia da empresa
# criar um dicionário com todos os solários dos funcionários
# para cada mudança, fazer um bfs que conta quantas
# """

from collections import defaultdict, deque


def main():
	def bfs():
		queue = deque([1])
		insatisfactions = 0

		while queue:
			employee = queue.popleft()
			boss = bosses[employee]

			for subordinate in hierarchy[employee]:
				queue.append(subordinate)

			if salaries[employee] > salaries[boss] and satisfaction[boss]:
				insatisfactions += 1
				satisfaction[bosses[employee]] = False

		return insatisfactions

	N = int(input())  # funcionários

	hierarchy = defaultdict(set)
	salaries = dict()
	bosses = dict()
	satisfaction = dict()

	for i in range(1, N + 1):
		C, S = [int(x) for x in input().split()]  # chefe, salário
		if C != i:
			hierarchy[C].add(i)

		bosses[i] = C
		satisfaction[i] = True
		salaries[i] = S

	A = int(input())  # ajustes

	changes = list()
	for _ in range(A):
		I, X = [int(x) for x in input().split()]  # funcionário, salário alterado
		changes.append((I, X))

	resultado = bfs()
	print(resultado)

	# após a mudança, checar se o status do chefe ou do empregado atual mudaram
	for emp, sal in changes:
		salaries[emp] = sal
		boss = bosses[emp]

		# status antigo do chefe e empregado
		old_boss, old_emp = satisfaction[boss], satisfaction[emp]

		# checa e muda o status do chefe
		if boss != emp:
			if sal > salaries[boss]:
				satisfaction[boss] = False
			else:
				satisfaction[boss] = True

		# checa e muda o status do empregado
		changed = False
		for subordinate in hierarchy[emp]:
			if salaries[subordinate] > salaries[emp]:
				changed = True
				satisfaction[emp] = False

		if not changed:
			satisfaction[emp] = True

		# checa se o número de insatisfação muda

		if old_boss == True and satisfaction[boss] == False:
			resultado += 1
		elif old_boss == False and satisfaction[boss] == True:
			resultado -= 1

		if boss != emp:
			if old_emp == True and satisfaction[emp] == False:
				resultado += 1
			elif old_emp == False and satisfaction[emp] == True:
				resultado -= 1

		print(resultado)


if __name__ == "__main__":
	main()
