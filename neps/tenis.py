"""
Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um nível de jogo, que é representado por um número inteiro: quanto maior o número, melhor o nível do jogador.

Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o jogo mais interessante, eles querem que os níveis dos dois times formados sejam o mais próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.

Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons em algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar a menor diferença possível entre os níveis dos times que podem ser formados?

Entrada
A entrada contém quatro linhas, cada linha contendo um inteiro A, B, C e D, indicando o nível de jogo dos quatro amigos.

Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, a menor diferença entre os níveis dos dois times formados.
"""

# níveis dos jogadores
a = int(input())
b = int(input())
c = int(input())
d = int(input())

niveis = list()
niveis.extend([a, b, c, d])
niveis.sort()

equipe1 = niveis[0] + niveis[3]
equipe2 = niveis[1] + niveis[2]

if equipe1 > equipe2:
	print(equipe1 - equipe2)
else:
	print(equipe2 - equipe1)
