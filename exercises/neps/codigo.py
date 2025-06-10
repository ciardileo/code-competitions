"""
numero representado pela quantidade de vezes que o 100 aparece
"""

n = int(input())

sequencia = "".join(input().split())

# print(sequencia)

qtd = 0
em_sequencia = False
for i in range(len(sequencia)):
	if sequencia[i] == "1" and not em_sequencia:
		em_sequencia = True
	# print("iniciei sequencia", sequencia[i], i)
	elif sequencia[i] == "0" and em_sequencia:
		if sequencia[i - 1] == "0":
			qtd += 1
			em_sequencia = False
		# print("terminei sequencia", sequencia[i], i)
	# print("continuei sequencia", sequencia[i], i)
	else:
		pass
	# print("quebrei sequencia", sequencia[i], i)
	# print("iniciei nova sequencia", sequencia[i], i)

print(qtd)

# ===============================
# versão do chatgpt:
"""
n = int(input())
sequencia = "".join(input().split())

qtd = 0
em_sequencia_de_uns = False

for i in range(len(sequencia) - 2):  # Subtrai 2 para evitar um IndexError
    if sequencia[i:i + 3] == "100":
        qtd += 1

print(qtd)
"""
