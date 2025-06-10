"""

"""


def main():
	S = int(input())
	A = int(input())
	B = int(input())

	result = 0

	for num in range(A, B + 1):
		total = 0
		for digit in str(num):
			total += int(digit)

		if total == S:
			result += 1

	print(result)


if __name__ == "__main__":
	main()
