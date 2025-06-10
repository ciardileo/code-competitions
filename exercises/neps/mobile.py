"""
verificar se um móbile é estável conforme o peso das bolas
A = B + C + D
B + C = D
B = C
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b == c and b + c == d and b + c + d == a:
	print("S")
else:
	print("N")

