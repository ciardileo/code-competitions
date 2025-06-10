"""
a cada dia árvores são plantadas
árvores ja plantadas produzem M mudas para serem plantadas no dia seguinte todos os dias
determinar em quantos dias a floresta tera A árvores

solução (pg):
2 -> 8 -> 32
1 -> 3 -> 9 -> 27
"""

def minimum_days(initial, k, target):
    n = -1
    element = 0
    while element < target:
        n += 1
        element = initial * (k ** n)
        
    return n

initial = int(input())
seeds = int(input()) 
target = int(input())

k = (initial + initial * seeds) / initial

print(minimum_days(initial, k, target))


