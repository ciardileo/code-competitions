"""
selection sorting
"""

# imports 
import random

"""
funciona com uma lógica de ponteiro:
pegue o primeiro número da lista e comece a comparar com todo o resto, ao final da iteração, caso tenha achado um número menor que o primeiro, troque o primeiro de posicão com esse menor número

"""

# valores
inteiros_unicos = random.sample(range(1, 101), 25)

print(inteiros_unicos)

def selection_sort(lista):
    for item_atual in range(len(lista)):
        menor_indice = item_atual
        
        for numero in range(item_atual, len(lista)):
            if lista[numero] < lista[menor_indice]:
                menor_indice = numero
        
        if menor_indice != item_atual:
            lista[item_atual], lista[menor_indice] = lista[menor_indice], lista[item_atual]
            
    return lista
        
print(selection_sort(inteiros_unicos))
            
        
