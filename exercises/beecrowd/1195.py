"""
Árvores binárias: 
Para cada caso, montar a árvore e apresentar o caminho Prefixo, infixo e posfixo
"""

from os import sep
from collections import defaultdict

def inserir(arvore, raiz, elemento):
    if elemento > raiz:
        if arvore[raiz][1] == None:
            arvore[raiz][1] = elemento
        else:
            inserir(arvore, arvore[raiz][1], elemento)
    else:
        if arvore[raiz][0] == None:
            arvore[raiz][0] = elemento
        else:
            inserir(arvore, arvore[raiz][0], elemento)


def pre(arvore: defaultdict, raiz, caminho: list): # raiz, esquerda, direita
    # adicionar todos os que visitar de primeira
    caminho.append(raiz)

    if arvore.get(raiz, -1) != -1 and arvore[raiz][0] != None:
        caminho = pre(arvore, arvore[raiz][0], caminho)

    if arvore.get(raiz, -1) != -1 and arvore[raiz][1] != None:
        caminho = pre(arvore, arvore[raiz][1], caminho)

    return caminho


def ordem(arvore: defaultdict, raiz, caminho: list):  # esquerda, raiz, direita
    if arvore.get(raiz, -1) == -1:
        caminho.append(raiz)
    else:
        if arvore[raiz][0] != None:
            caminho = ordem(arvore, arvore[raiz][0], caminho)

        caminho.append(raiz)

        if arvore[raiz][1] != None:
            caminho = ordem(arvore, arvore[raiz][1], caminho)

    return caminho


def pos(arvore: defaultdict, raiz, caminho: list):  # esquerda, raiz, direita
    # print(raiz)
    # tem filhos? se não, printa agora
    if arvore.get(raiz, -1) == -1:
        caminho.append(raiz)
    else:
        # vai até o final da esquerda
        if arvore[raiz][0] != None:
            caminho = pos(arvore, arvore[raiz][0], caminho)

        # vai até o final da direita
        if arvore[raiz][1] != None:
            caminho = pos(arvore, arvore[raiz][1], caminho)

        # adiciona a raiz quando terminar de ver toda sua subarvore
        caminho.append(raiz)

    return caminho

def main():
    C = int(input())  # número de casos

    for i in range(C):
        N = int(input())  # número de elementos da árvore
        nodes = list(map(int, input().split()))
        arvore = defaultdict(lambda: [None, None])
        raiz = nodes[0]
        
        for k in range(1, N):
            inserir(arvore, raiz, nodes[k])

        print(f"Case {i + 1}:")

        # pré-ordem
        print("Pre.:", end=" ")
        print(*pre(arvore, raiz, []), sep=" ")

        # em ordem
        print("In..:", end=" ")
        print(*ordem(arvore, raiz, []), sep=" ")

        # em ordem
        print("Post:", end=" ")
        print(*pos(arvore, raiz, []), sep=" ")

        print()


if __name__ == "__main__":
    main()