"""
Um dos algoritmos de busca mais populares, baseado no pricípio de divisão e conquista.
Algoritmos de divisão e conquista funcionam dividindo problemas em subproblemas, quebrando arrays pela metade


Divide:
A divisão não é feita de maneira física, e sim de maneira lógica, apenas guardando as posições de início, fim e meio.
If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r]

Conquer:
In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.
"""

import random

# divide a string e usa o merge pra juntar e ordenar
def merge_sort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array)
        
    # se o problema ainda não for unitário
    if fim - inicio > 1:
        meio = (fim + inicio) // 2 # divisão inteira pra fazer a divisão caso seja ímpar
        merge_sort(array, inicio, meio)
        merge_sort(array, meio, fim)
        merge(array, inicio, meio, fim)


def merge(array, inicio, meio, fim):
    esquerda = array[inicio:meio]
    direita = array[meio:fim]
    menor_esquerda, menor_direita = 0, 0
    
    for k in range(inicio, fim):
        # verifica se a lista da esquerda ou da direit ja foi "esvaziada"
        if menor_esquerda >= len(esquerda):
            array[k] = direita[menor_direita]
            menor_direita += 1
        elif menor_direita >= len(direita):
            array[k] = esquerda[menor_esquerda]
            menor_esquerda += 1
            
        # adicionando na lista conforme o menor número na posição na lista da direita e da esquerda
        elif esquerda[menor_esquerda] < direita[menor_direita]:
            array[k] = esquerda[menor_esquerda]
            menor_esquerda += 1
        else:
            array[k] = direita[menor_direita]
            menor_direita += 1
            
            
if __name__ == '__main__':
    lista = random.sample(range(1, 1000), 50)
    print(lista)
    print('-'*25)
    
    merge_sort(lista)
    
    print(lista)