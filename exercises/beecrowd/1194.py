"""
PRE ORDEM: ROOT LEFT RIGHT
EM ORDEM: LEFT ROOT RIGHT
POS ORDEM: LEFT RIGHT ROOT
"""

preorder = ["A", "B", "D", "E", "C", "F"]
inorder = ["D", "B", "E", "A", "C", "F"]

def build_tree(preorder, inorder):
    # encontra a raiz
    raiz = preorder[0]

    # tamanhos da subarvore esquerda e direita
    nodes = len(inorder)

    # calcular tamanho de cada subarvore
    indice_raiz = 0
    for i in range(nodes):
        if inorder[i] == raiz:
            indice_raiz = i
            break
    
    count_esq = indice_raiz
    count_dir = nodes - count_esq - 1

    if count_esq > 0:
        left = build_tree(preorder[1:(count_esq + 1)], inorder[:count_esq])
    else:
        left = None

    if count_dir > 0:
        right = build_tree(preorder[(count_esq + 1):], inorder[(count_esq + 1):])
    else:
        right = None

    return [raiz, left, right]
    


print(*build_tree(preorder, inorder), sep="\n")
            

# from sys import stdin
# input = lambda: stdin.readline().rstrip()

# class Node:
#     __slots__ = ("val", "esq", "dir")
#     def __init__(self, val):
#         self.val = val
#         self.esq = None
#         self.dir = None


# def main():
#     # casos de teste
#     C = int(input())

#     for _ in range(C):
#         nodes, preordem, emordem = input().split()

#         arvore = Node(preordem[0])

# if __name__ == "__main__":
#     main()