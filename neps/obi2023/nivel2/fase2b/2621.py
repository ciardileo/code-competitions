"""
dados o número de estudantes, a posição inicial de bruno e a quantidade de palmas, determinar a posição dele
"""


def main():
	N = int(input())  # alunos
	I = int(input())  # posição inicial
	P = int(input())  # palmas do professor

	result = (I + P) % N

	print(result if result > 0 else N)


if __name__ == "__main__":
	main()
