"""
estudar sobre a técnica de janelas deslizantes
"""


def main():
	total = int(input())
	sequence = []

	for i in range(total):
		sequence.append((int(input())))

	max_length = 0
	first = 0
	current_set = set()

	for num in range(len(sequence)):
		# caso achar alguma repetição, começa a limpar o set desde o começo até não haver mais repetição
		while sequence[num] in current_set:
			current_set.remove(sequence[first])
			first += 1
		current_set.add(sequence[num])
		max_length = max(max_length, num - first + 1)

	print(max_length)


if __name__ == "__main__":
	main()
