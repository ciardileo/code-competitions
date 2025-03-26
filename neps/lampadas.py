"""
lampadas A e B
interruptores i1 e i2
se aperta i1 muda o estado da A
se aperta i2 as duas mudam de estado
"""

a = False
b = False


def i1():
	global a
	if not a:
		a = True
	else:
		a = False


def i2():
	global b
	i1()

	if not b:
		b = True
	else:
		b = False


n = int(input())
sequencia = [int(x) for x in input().split()]

for i in sequencia:
	if i == 1:
		i1()
	else:
		i2()

print(1 if a else 0)
print(1 if b else 0)
